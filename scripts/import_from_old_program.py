#!/usr/bin/env python

from django.contrib.auth.models import User
from django.db import transaction

from memorizing.flashcards.models import CardList, Card

from datetime import datetime
from optparse import OptionParser
import os

@transaction.commit_manually
def main(filename, username):
    user = User.objects.get(username=username)
    name = os.path.basename(filename).split('.')[0].capitalize()
    print name
    cardlist = CardList(user=user, name=name)
    cardlist.save()
    now = datetime.now()
    f = open(filename)
    while f:
        word = f.readline().strip()
        if not word:
            break
        text = f.readline().strip()
        _ = f.readline()
        # I don't care enough to preserve the old dates.
        _ = f.readline()
        _ = f.readline()
        card = Card(list=cardlist, word=word, text=text, last_reviewed=now,
                date_entered=now)
        card.save()
        cardlist.total_difficulty += card.average_difficulty
        cardlist.save()
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
