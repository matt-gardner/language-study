#!/usr/bin/env python

import os, sys

sys.path.append(os.curdir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorizing.settings'

from django.contrib.auth.models import User
from memorizing.flashcards.models import *

# vim: et sw=4 sts=4
