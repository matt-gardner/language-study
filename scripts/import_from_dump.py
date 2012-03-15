#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.fields import DateTimeField # a bit of a hack...

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
        languages[language['pk']] = Language(name=language['fields']['name'],
                module_name=language['fields']['module_name'])
        languages[language['pk']].save()
    declensions = dict()
    for d in types.get('drills.declension', []):
        declensions[d['pk']] = Declension(name=d['fields']['name'],
                language=languages[d['fields']['language']])
        declensions[d['pk']].save()
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
    declinabletypes = dict()
    for dt in types.get('drills.declinabletype', []):
        declinabletypes[dt['pk']] = DeclinableType(name=dt['fields']['name'],
                language=languages[dt['fields']['language']])
        declinabletypes[dt['pk']].save()
    conjugations = dict()
    for c in types.get('drills.conjugation', []):
        conjugations[c['pk']] = Conjugation(name=c['fields']['name'],
                language=languages[c['fields']['language']])
        conjugations[c['pk']].save()
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
    tags = dict()
    for tag in types.get('drills.tag', []):
        args = dict()
        args['wordlist'] = wordlists[tag['fields']['wordlist']]
        args['name'] = tag['fields']['name']
        tags[tag['pk']] = Tag(**args)
        tags[tag['pk']].save()
    # Now words
    words = dict()
    for word in types.get('drills.word', []):
        word_pk = word['pk']
        word = word['fields']
        args = dict()
        args['wordlist'] = wordlists[word['wordlist']]
        args['word'] = word['word']
        args['definition'] = word['definition']
        args['date_entered'] = word.get('date_entered', now)
        args['last_reviewed'] = word.get('last_reviewed', now)
        args['last_wrong'] = word.get('last_wrong', now)
        # Try to handle the old "average_difficulty" field gracefully
        if 'average_difficulty' in word:
            difficulty = word['average_difficulty']
            if difficulty < 1:
                memory_index = 9
            elif difficulty < 2:
                memory_index = 8
            elif difficulty < 5:
                memory_index = 7
            elif difficulty < 10:
                memory_index = 6
            elif difficulty < 20:
                memory_index = 5
            elif difficulty < 25:
                memory_index = 4
            elif difficulty < 30:
                memory_index = 3
            else:
                memory_index = 0
            args['memory_index'] = memory_index
            # HACK!  This is to get a datetime object without having to parse
            # the string myself.
            hack = DateTimeField()
            last_reviewed = hack.to_python(args['last_reviewed'])
            args['next_review'] = (last_reviewed +
                    Word.REVIEW_PERIODS[memory_index][1])
        else:
            args['memory_index'] = word.get('memory_index', 0)
            args['next_review'] = word.get('next_review', now)
        args['review_count'] = word.get('review_count', 0)
        words[word_pk] = Word(**args)
        words[word_pk].save()
        for tag_id in word['tags']:
            w.tags.add(tags[tag_id])
    # Verbs
    for verb in types.get('drills.verb', []):
        verb = verb['fields']
        args = dict()
        args['wordlist'] = wordlists[verb['wordlist']]
        args['conjugation'] = conjugations[verb['conjugation']]
        args['word'] = words[verb['word']]
        v = Verb(**args)
        v.save()
    # Declinable words
    for dw in types.get('drills.declinableword', []):
        dw = dw['fields']
        args = dict()
        args['wordlist'] = wordlists[dw['wordlist']]
        args['declension'] = declensions[dw['declension']]
        args['type'] = declinabletypes[dw['type']]
        args['word'] = words[dw['word']]
        d = DeclinableWord(**args)
        d.save()
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
