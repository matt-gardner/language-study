from django.db import models

from language_study.drills.models import DeclinableWord

# Slovene-specific irregular declension stuff
#############################################

# If the final vowel of a stem gets dropped before adding the case endings, set
# this as true.
class FleetingVowel(models.Model):
    declinable = models.OneToOneField('drills.DeclinableWord')
    class Meta:
        app_label = 'slovene'

# This only applies to first declension (masculine) nouns and their modifiers.
# It's completely ignored in other declensions.
class Animate(models.Model):
    declinable = models.OneToOneField('drills.DeclinableWord')
    class Meta:
        app_label = 'slovene'
