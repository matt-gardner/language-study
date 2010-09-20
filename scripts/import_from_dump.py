#!/usr/bin/env python

import os, sys

sys.path.append(os.curdir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorizing.settings'

from django.contrib.auth.models import User
from django.db import transaction

from memorizing.flashcards.models import CardList, Card

from datetime import datetime
from optparse import OptionParser
import os, cjson

@transaction.commit_manually
def main(filename, username):
    user = User.objects.get(username=username)
    json = cjson.decode(open(filename).read())
    json_index = 0
    cardlists = dict()
    while json[json_index]['model'] == 'flashcards.cardlist':
        list = json[json_index]
        cardlists[list['pk']] = CardList(user=user, name=list['fields']['name'])
        cardlists[list['pk']].save()
        json_index += 1
    now = datetime.now()
    hard = Card.DIFFICULTY_SCORES['hard']
    for item in json[json_index:]:
        card = item['fields']
        args = dict()
        args['list'] = cardlists[card['list']]
        args['word'] = card['word']
        args['text'] = card['text']
        args['last_reviewed'] = card.get('last_reviewed', now)
        args['date_entered'] = card.get('date_entered', now)
        args['average_difficulty'] = card.get('average_difficulty', hard)
        args['review_count'] = card.get('review_count', 0)
        card = Card(**args)
        card.save()
    transaction.commit()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--file',
            dest='file',
            help='Path to old .mem file',
            )
    parser.add_option('-u', '--user',
            dest='user',
            help='Username for user to add the list for',
            )
    options, args = parser.parse_args()
    main(options.file, options.user)

# vim: et sw=4 sts=4
