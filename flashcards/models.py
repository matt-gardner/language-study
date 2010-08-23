from django.db import models

class CardList(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=128)


class Card(models.Model):
    DIFFICULTY_SCORES = {
            'Easy': 1,
            'Medium': 5,
            'Hard': 10,
            }
    list = models.ForeignKey('CardList')
    word = models.CharField(max_length=128)
    text = models.CharField(max_length=4096)
    last_reviewed = models.DateTimeField()
    date_entered = models.DateTimeField()
    average_difficulty = models.FloatField(default=DIFFICULTY_SCORES['Hard'])


# vim: et sts=4 sw=4
