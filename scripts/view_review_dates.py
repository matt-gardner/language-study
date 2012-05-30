#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from language_study.drills.models import Word

from collections import defaultdict
from datetime import datetime, timedelta
from optparse import OptionParser

def main(username, listname, words_per_day, days_to_add, words_per_minute):
    user = User.objects.get(username=username)
    wordlist = user.wordlist_set.get(name=listname)
    words = wordlist.word_set.all()
    review_dates = defaultdict(int)
    now = datetime.now()
    today = now.strftime('%m/%d/%Y')
    tomorrow = (now+timedelta(1)).strftime('%m/%d/%Y')
    ending_time = now+timedelta(30*3)
    transitive_review_dates = defaultdict(int)
    projected_review_dates = defaultdict(int)
    periods = Word.REVIEW_PERIODS
    date_date_str = dict()
    for w in words:
        date = w.next_review
        date_str = date.strftime('%m/%d/%Y')
        if date > ending_time:
            continue
        if date_str == today or date_str == tomorrow:
            date_str = w.next_review.strftime('%m/%d/%Y %H')
        review_dates[date_str] += 1
        i = w.memory_index
        new_time = w.next_review
        while i < len(periods)-1:
            i += 1
            new_time = new_time + periods[i][1]
            if new_time > ending_time:
                break
            date_str = new_time.strftime('%m/%d/%Y')
            if date_str == today or date_str == tomorrow:
                date_str = new_time.strftime('%m/%d/%Y %H')
            transitive_review_dates[date_str] += 1
    for i in range(days_to_add):
        for w in range(words_per_day):
            new_time = now + timedelta(i)
            j = 0
            while j < len(periods)-1:
                j += 1
                new_time = new_time + periods[j][1]
                if new_time > ending_time:
                    break
                date_str = new_time.strftime('%m/%d/%Y')
                if date_str == today or date_str == tomorrow:
                    date_str = new_time.strftime('%m/%d/%Y %H')
                projected_review_dates[date_str] += 1
    dates = set(review_dates.keys())
    dates.update(transitive_review_dates.keys())
    dates = list(dates)
    dates.sort(key=date_to_number)
    for d in dates:
        total = (review_dates[d] + transitive_review_dates[d] +
                projected_review_dates[d])
        projected_time = total / float(words_per_minute)
        print '%15s: %3d (%3d %3d %3d): %3.1f minutes: ' % (d,
                total,
                review_dates[d],
                transitive_review_dates[d],
                projected_review_dates[d],
                projected_time)


def date_to_number(date_str):
    fields = date_str.split()
    if len(fields) == 2:
        date, hour = fields
    else:
        date = fields[0]
        hour = 0
    month, day, year = [int(x) for x in date.split('/')]
    return year * 365 + month * 30 + day + float(hour) / 24


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-u', '--user',
            default='matt',
            dest='user',
            help='Username to look for the list')
    parser.add_option('-l', '--list',
            default='Slovene',
            dest='list',
            help='Name of the list to show review dates for')
    parser.add_option('-n', '--num-words',
            default=30,
            type=int,
            dest='num_words',
            help='Number of words added per day')
    parser.add_option('-d', '--num-days',
            default=7,
            type=int,
            dest='num_days',
            help='Number of days to continue adding words')
    parser.add_option('-m', '--words-per-minute',
            default=8,
            type=int,
            dest='words_per_minute',
            help='Average number of words reviewed per minute')
    opts, args = parser.parse_args()
    if not opts.user or not opts.list:
        print 'Usage: view_review_dates.py -u [user] -l [list]'
        sys.exit(-1)
    main(opts.user, opts.list, opts.num_words, opts.num_days,
            opts.words_per_minute)

# vim: et sw=4 sts=4
