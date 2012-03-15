from django.db import models

from datetime import datetime, timedelta


# Language Models
#################

class Language(models.Model):
    name = models.CharField(max_length=128, unique=True)
    module_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Declension(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class DeclinableType(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Number(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Conjugation(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Tense(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Voice(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Mood(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return self.name


# Drilling Models
#################

# We have some redundancy in the way this is set up (i.e., a foreign key that
# could be retrieved by just doing a join on a key that's already present, like
# ConjugationDrillResult pointing to both the verb and the wordlist), but I
# figured that the easier lookups and aggregrations would be worth having a
# little redundancy, because we will be careful to only modify the database in
# valid ways.


class WordList(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=128)
    language = models.ForeignKey('Language')

    def __unicode__(self):
        return u'%s: %s' % (self.user.first_name, self.name)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    wordlist = models.ForeignKey('WordList')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Word(models.Model):
    REVIEW_PERIODS = [
            ('1 minute', timedelta(0, 60)),
            ('10 minutes', timedelta(0, 600)),
            ('1 hour', timedelta(0, 3600)),
            ('5 hours', timedelta(0, 18000)),
            ('1 day', timedelta(1)),
            ('4 days', timedelta(4)),
            ('2 weeks', timedelta(14)),
            ('1 month', timedelta(30)),
            ('4 months', timedelta(120)),
            ('1 year', timedelta(365)),
            ]
    wordlist = models.ForeignKey('WordList')
    word = models.CharField(max_length=128)
    definition = models.CharField(max_length=4096)
    date_entered = models.DateTimeField()
    last_reviewed = models.DateTimeField()
    last_wrong = models.DateTimeField()
    memory_index = models.IntegerField(default=0)
    next_review = models.DateTimeField()
    review_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')

    def reviewed(self, correct=None):
        now = datetime.now()
        if correct == True:
            time_in_memory = now - self.last_wrong
            if time_in_memory > Word.REVIEW_PERIODS[self.memory_index][1]:
                self.memory_index += 1
        elif correct == False:
            self.memory_index = 0
            self.last_wrong = now
        self.last_reviewed = now
        self.next_review = now + Word.REVIEW_PERIODS[self.memory_index][1]
        self.review_count += 1
        self.save()

    def __unicode__(self):
        return u'%s: %s' % (self.wordlist.name, self.word)


# Verb stuff (including irregulars)
###################################

class Verb(models.Model):
    word = models.OneToOneField('Word')
    wordlist = models.ForeignKey('WordList') # duplicate, but speeds things up
    conjugation = models.ForeignKey('Conjugation')


class IrregularVerbForm(models.Model):
    verb = models.ForeignKey('Verb')
    person = models.ForeignKey('Person')
    number = models.ForeignKey('Number')
    tense = models.ForeignKey('Tense')
    mood = models.ForeignKey('Mood')
    voice = models.ForeignKey('Voice')
    form = models.CharField(max_length=128)


class IrregularVerbStem(models.Model):
    verb = models.ForeignKey('Verb')
    tense = models.ForeignKey('Tense')
    mood = models.ForeignKey('Mood')
    voice = models.ForeignKey('Voice')
    stem = models.CharField(max_length=128)


# Maybe this should be in attic_greek/models.py?
class IrregularVerbAugmentedStem(models.Model):
    verb = models.ForeignKey('Verb')
    tense = models.ForeignKey('Tense')
    stem = models.CharField(max_length=128)


class VerbTenseWithNoPassive(models.Model):
    verb = models.ForeignKey('Verb')
    tense = models.ForeignKey('Tense')


# Declension stuff (including irregulars)
#########################################

class DeclinableWord(models.Model):
    word = models.OneToOneField('Word')
    wordlist = models.ForeignKey('WordList') # duplicate, but speeds things up
    declension = models.ForeignKey('Declension')
    type = models.ForeignKey('DeclinableType')

    def __unicode__(self):
        return self.word.word


class IrregularDeclinableForm(models.Model):
    declinable = models.ForeignKey('DeclinableWord')
    gender = models.ForeignKey('Gender')
    number = models.ForeignKey('Number')
    case = models.ForeignKey('Case')
    form = models.CharField(max_length=128)


# Maybe this should be in attic_greek/models.py?
class LongPenult(models.Model):
    declinable = models.OneToOneField('DeclinableWord')


# Drilling statistics
#####################

class ConjugationDrillResult(models.Model):
    wordlist = models.ForeignKey('WordList')
    verb = models.ForeignKey('Verb')
    conjugation = models.ForeignKey('Conjugation')
    person = models.ForeignKey('Person')
    number = models.ForeignKey('Number')
    tense = models.ForeignKey('Tense')
    mood = models.ForeignKey('Mood')
    voice = models.ForeignKey('Voice')
    correct = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)


class DeclensionDrillResult(models.Model):
    wordlist = models.ForeignKey('WordList')
    word = models.ForeignKey('DeclinableWord')
    type = models.ForeignKey('DeclinableType')
    declension = models.ForeignKey('Declension')
    gender = models.ForeignKey('Gender')
    number = models.ForeignKey('Number')
    case = models.ForeignKey('Case')
    correct = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)


# vim: et sts=4 sw=4
