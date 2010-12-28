#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from django.db import transaction

from language_study.drills.models import WordList, Word, Tag

from datetime import datetime
from optparse import OptionParser
import os, cjson

@transaction.commit_manually
def main(filename, username):
    user = User.objects.get(username=username)
    json = cjson.decode(open(filename).read())
    json_index = 0
    lists = []
    words = []
    tags_ = []
    for item in json:
        if item['model'] == 'drills.wordlist':
            lists.append(item)
        elif item['model'] == 'drills.word':
            words.append(item)
        elif item['model'] == 'drills.tag':
            tags_.append(item)
    wordlists = dict()
    for wordlist in lists:
        wordlists[wordlist['pk']] = WordList(user=user,
                name=wordlist['fields']['name'])
        wordlists[wordlist['pk']].save()
    now = datetime.now()
    hard = Word.DIFFICULTY_SCORES['hard']
    tags = dict()
    for tag in tags_:
        args = dict()
        args['wordlist'] = wordlists[tag['fields']['wordlist']]
        args['name'] = tag['fields']['name']
        tags[tag['pk']] = Tag(**args)
        tags[tag['pk']].save()
    for word in words:
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
