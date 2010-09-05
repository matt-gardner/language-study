from django.db import models

from datetime import datetime

class CardList(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=128)
    total_difficulty = models.FloatField(default=0)

    def __unicode__(self):
        return u'%s: %s' % (self.user.first_name, self.name)


class Card(models.Model):
    DIFFICULTY_SCORES = {
            'easy': 1,
            'medium': 20,
            'hard': 40,
            }
    DIFFICULTY_ALPHA = .4
    list = models.ForeignKey('CardList')
    word = models.CharField(max_length=128)
    text = models.CharField(max_length=4096)
    last_reviewed = models.DateTimeField()
    date_entered = models.DateTimeField()
    average_difficulty = models.FloatField(default=DIFFICULTY_SCORES['hard'])

    def update_difficulty(self, score):
        old = self.average_difficulty
        alpha = Card.DIFFICULTY_ALPHA
        new = (1 - alpha) * self.average_difficulty + alpha * score
        self.average_difficulty = new
        self.save()
        difference = new - old
        self.list.total_difficulty += difference
        self.list.save()

    def reviewed(self):
        self.last_reviewed = datetime.now()
        self.save()

    def __unicode__(self):
        return u'%s: %s' % (self.list.name, self.word)



# vim: et sts=4 sw=4
