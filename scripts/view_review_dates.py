#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from language_study.drills.models import *

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser

def main(username, listname):
    user = User.objects.get(username=username)
    wordlist = user.wordlist_set.get(name=listname)
    words = wordlist.word_set.all()
    review_dates = defaultdict(int)
    today = datetime.now().strftime('%m/%d/%Y')
    for w in words:
        date_str = w.next_review.strftime('%m/%d/%Y')
        if date_str == today:
            date_str = w.next_review.strftime('%m/%d/%Y %H')
        review_dates[date_str] += 1
    dates = review_dates.keys()
    dates.sort()
    for d in dates:
        print '%s: %d' % (d, review_dates[d])


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-u', '--user',
            default='',
            dest='user',
            help='Username to look for the list')
    parser.add_option('-l', '--list',
            default='',
            dest='list',
            help='Name of the list to show review dates for')
    opts, args = parser.parse_args()
    if not opts.user or not opts.list:
        print 'Usage: view_review_dates.py -u [user] -l [list]'
        sys.exit(-1)
    main(opts.user, opts.list)

# vim: et sw=4 sts=4
