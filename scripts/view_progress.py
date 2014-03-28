#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from language_study.drills.models import Word

from collections import defaultdict
from optparse import OptionParser

def main(username, listname):
    user = User.objects.get(username=username)
    wordlist = user.wordlist_set.get(name=listname)
    words = wordlist.word_set.all()
    words_per_period = defaultdict(int)
    periods = Word.REVIEW_PERIODS
    total = 0
    for w in words:
        words_per_period[w.memory_index] += 1
        total += 1
    pers = words_per_period.keys()
    pers.sort()
    for p in pers:
        print '%10s: %4d' % (periods[p][0], words_per_period[p])
    print 'Total:', total


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-u', '--user',
            default='matt',
            dest='user',
            help='Username to look for the list')
    parser.add_option('-l', '--list',
            default='Slovene (auto)',
            dest='list',
            help='Name of the list to show review dates for')
    opts, args = parser.parse_args()
    if not opts.user or not opts.list:
        print 'Usage: view_review_dates.py -u [user] -l [list]'
        sys.exit(-1)
    main(opts.user, opts.list)

# vim: et sw=4 sts=4
