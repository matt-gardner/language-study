from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title


class BookTranslation(models.Model):
    book = models.ForeignKey('Book')
    language = models.ForeignKey('drills.Language')

    def __unicode__(self):
        return self.book.title + ': ' + self.language.name


class Page(models.Model):
    book = models.ForeignKey('BookTranslation')
    chapter = models.IntegerField() # should this be a foreign key instead?
    # For books without pages, just put each chapter's text in a single page
    page_number = models.IntegerField()
    image_path = models.CharField(max_length=256, blank=True)
    text = models.TextField()

    def __unicode__(self):
        return unicode(self.book) + ", page " + str(self.page_number)

    class Meta:
        ordering = ['page_number']


# Create your models here.
