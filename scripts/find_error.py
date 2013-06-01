#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.contrib.auth.models import User
from language_study.drills.models import *
from language_study.reading.models import *


def main():
    name = 'Slovene (auto)'
    l = WordList.objects.get(name=name)
    total_words = Word.objects.count()
    error = False
    for i in range(total_words):
        try:
            word = l.word_set.get(pk=i)
        except Word.DoesNotExist:
            pass
        except UnicodeDecodeError:
            error = True
            print 'Error found in word with pk', i
    if not error:
        print 'No error found'


if __name__ == '__main__':
    main()

# vim: et sw=4 sts=4
