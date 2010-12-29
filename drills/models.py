from django.db import models

from datetime import datetime


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


class DeclinableType(models.Model):
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
    DIFFICULTY_SCORES = {
            'easy': 1,
            'medium': 20,
            'hard': 40,
            }
    DIFFICULTY_ALPHA = .4
    wordlist = models.ForeignKey('WordList')
    word = models.CharField(max_length=128)
    definition = models.CharField(max_length=4096)
    last_reviewed = models.DateTimeField()
    date_entered = models.DateTimeField(auto_now_add=True)
    average_difficulty = models.FloatField(default=DIFFICULTY_SCORES['hard'])
    review_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')

    def update_difficulty(self, score):
        old = self.average_difficulty
        alpha = Word.DIFFICULTY_ALPHA
        new = (1 - alpha) * self.average_difficulty + alpha * score
        self.average_difficulty = new
        self.save()
        difference = new - old
        self.wordlist.save()

    def reviewed(self):
        self.last_reviewed = datetime.now()
        self.review_count += 1
        self.save()

    def __unicode__(self):
        return u'%s: %s' % (self.wordlist.name, self.word)


class Verb(Word):
    conjugation = models.ForeignKey('Conjugation')


class DeclinableWord(Word):
    declension = models.ForeignKey('Declension')
    type = models.ForeignKey('DeclinableType')


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
