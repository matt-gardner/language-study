#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from django.db import transaction

from language_study.drills.models import *

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser
import os, cjson

@transaction.commit_manually
def main(filename, username):
    user = User.objects.get(username=username)
    json = cjson.decode(open(filename).read())
    json_index = 0
    types = defaultdict(list)
    # Organize the JSON dump by model type
    for item in json:
        types[item['model']].append(item)
    # Rebuild the models in the necessary order
    # Languages and associated models first
    languages = dict()
    for language in types.get('drills.language', []):
        languages[language['pk']] = Language(name=language['fields']['name'])
        languages[language['pk']].save()
    for declension in types.get('drills.declension', []):
        x = Declension(name=declension['fields']['name'],
                language=languages[declension['fields']['language']])
        x.save()
    for case in types.get('drills.case', []):
        x = Case(name=case['fields']['name'],
                language=languages[case['fields']['language']])
        x.save()
    for number in types.get('drills.number', []):
        x = Number(name=number['fields']['name'],
                language=languages[number['fields']['language']])
        x.save()
    for gender in types.get('drills.gender', []):
        x = Gender(name=gender['fields']['name'],
                language=languages[gender['fields']['language']])
        x.save()
    for denclinabletype in types.get('drills.denclinabletype', []):
        x = DeclinableType(name=denclinabletype['fields']['name'],
                language=languages[denclinabletype['fields']['language']])
        x.save()
    for conjugation in types.get('drills.conjugation', []):
        x = Conjugation(name=conjugation['fields']['name'],
                language=languages[conjugation['fields']['language']])
        x.save()
    for person in types.get('drills.person', []):
        x = Person(name=person['fields']['name'],
                language=languages[person['fields']['language']])
        x.save()
    for tense in types.get('drills.tense', []):
        x = Tense(name=tense['fields']['name'],
                language=languages[tense['fields']['language']])
        x.save()
    for voice in types.get('drills.voice', []):
        x = Voice(name=voice['fields']['name'],
                language=languages[voice['fields']['language']])
        x.save()
    for mood in types.get('drills.mood', []):
        x = Mood(name=mood['fields']['name'],
                language=languages[mood['fields']['language']])
        x.save()
    # Then users (TODO)
    # Then word lists and tags
    wordlists = dict()
    for wordlist in types.get('drills.wordlist', []):
        wordlists[wordlist['pk']] = WordList(user=user,
                name=wordlist['fields']['name'],
                language=languages[wordlist['fields']['language']])
        wordlists[wordlist['pk']].save()
    now = datetime.now()
    hard = Word.DIFFICULTY_SCORES['hard']
    tags = dict()
    for tag in types.get('drills.tag', []):
        args = dict()
        args['wordlist'] = wordlists[tag['fields']['wordlist']]
        args['name'] = tag['fields']['name']
        tags[tag['pk']] = Tag(**args)
        tags[tag['pk']].save()
    # Then the words themselves
    for word in types.get('drills.word', []):
        word = word['fields']
        args = dict()
        args['wordlist'] = wordlists[word['wordlist']]
        args['word'] = word['word']
        args['definition'] = word['definition']
        args['last_reviewed'] = word.get('last_reviewed', now)
        # This is ignored because of auto_now_add
        #args['date_entered'] = word.get('date_entered', now)
        args['average_difficulty'] = word.get('average_difficulty', hard)
        args['review_count'] = word.get('review_count', 0)
        w = Word(**args)
        w.save()
        for tag_id in word['tags']:
            w.tags.add(tags[tag_id])
    # And finally the stats (TODO)
    transaction.commit()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--file',
            dest='file',
            help='Path to database dump file',
            )
    parser.add_option('-u', '--user',
            dest='user',
            help="Username for user to add the lists for (this doesn't"
            " currently support copying the user information)",
            )
    options, args = parser.parse_args()
    main(options.file, options.user)

# vim: et sw=4 sts=4
