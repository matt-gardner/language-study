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
    # Match verbs and declinable words with data from the words, removing the
    # word so we can insert just once
    for verb in types.get('drills.verb', []):
        pk = verb['pk']
        # this is slow, but we don't run this script much, so it's ok
        for word in types['drills.word']:
            if word['pk'] == pk:
                w = word
                break
        verb['fields'].update(w['fields'])
        types['drills.word'].remove(w)
    for dw in types.get('drills.declinableword', []):
        pk = dw['pk']
        # this is slow, but we don't run this script much, so it's ok
        for word in types['drills.word']:
            if word['pk'] == pk:
                w = word
                break
        dw['fields'].update(w['fields'])
        types['drills.word'].remove(w)
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
    for dt in types.get('drills.denclinabletype', []):
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
    for verb in types.get('drills.verb', []):
        verb = verb['fields']
        args = dict()
        args['conjugation'] = conjugations[verb['conjugation']]
        args['wordlist'] = wordlists[verb['wordlist']]
        args['word'] = verb['word']
        args['definition'] = verb['definition']
        args['last_reviewed'] = verb.get('last_reviewed', now)
        # This is ignored because of auto_now_add
        #args['date_entered'] = verb.get('date_entered', now)
        args['average_difficulty'] = verb.get('average_difficulty', hard)
        args['review_count'] = verb.get('review_count', 0)
        v = Verb(**args)
        v.save()
        for tag_id in verb['tags']:
            v.tags.add(tags[tag_id])
    for dw in types.get('drills.declinableword', []):
        dw = dw['fields']
        args = dict()
        args['declension'] = declensions[dw['declension']]
        args['type'] = declinabletypes[dw['type']]
        args['wordlist'] = wordlists[dw['wordlist']]
        args['word'] = dw['word']
        args['definition'] = dw['definition']
        args['last_reviewed'] = dw.get('last_reviewed', now)
        # This is ignored because of auto_now_add
        #args['date_entered'] = dw.get('date_entered', now)
        args['average_difficulty'] = dw.get('average_difficulty', hard)
        args['review_count'] = dw.get('review_count', 0)
        d = DeclinableWord(**args)
        d.save()
        for tag_id in dw['tags']:
            d.tags.add(tags[tag_id])
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
