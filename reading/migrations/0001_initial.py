# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'reading_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'reading', ['Book'])

        # Adding model 'BookTranslation'
        db.create_table(u'reading_booktranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reading.Book'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'reading', ['BookTranslation'])

        # Adding model 'Page'
        db.create_table(u'reading_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reading.BookTranslation'])),
            ('chapter', self.gf('django.db.models.fields.IntegerField')()),
            ('page_number', self.gf('django.db.models.fields.IntegerField')()),
            ('image_path', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reading', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'reading_book')

        # Deleting model 'BookTranslation'
        db.delete_table(u'reading_booktranslation')

        # Deleting model 'Page'
        db.delete_table(u'reading_page')


    models = {
        u'drills.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'reading.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'reading.booktranslation': {
            'Meta': {'object_name': 'BookTranslation'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reading.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"})
        },
        u'reading.page': {
            'Meta': {'ordering': "['page_number']", 'object_name': 'Page'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reading.BookTranslation']"}),
            'chapter': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'page_number': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reading']