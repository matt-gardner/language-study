# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Word.description'
        db.add_column(u'drills_word', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Word.description'
        db.delete_column(u'drills_word', 'description')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'drills.case': {
            'Meta': {'object_name': 'Case'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.conjugation': {
            'Meta': {'object_name': 'Conjugation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.conjugationdrillresult': {
            'Meta': {'object_name': 'ConjugationDrillResult'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Conjugation']"}),
            'correct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Mood']"}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Number']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Person']"}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Tense']"}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Verb']"}),
            'voice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Voice']"}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.declension': {
            'Meta': {'object_name': 'Declension'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.declensiondrillresult': {
            'Meta': {'object_name': 'DeclensionDrillResult'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Case']"}),
            'correct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'declension': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Declension']"}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Number']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.DeclinableType']"}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.DeclinableWord']"}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.declinabletype': {
            'Meta': {'object_name': 'DeclinableType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.declinableword': {
            'Meta': {'object_name': 'DeclinableWord'},
            'declension': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Declension']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.DeclinableType']"}),
            'word': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['drills.Word']", 'unique': 'True'}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.irregulardeclinableform': {
            'Meta': {'object_name': 'IrregularDeclinableForm'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Case']"}),
            'declinable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.DeclinableWord']"}),
            'form': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Number']"})
        },
        u'drills.irregularverbaugmentedstem': {
            'Meta': {'object_name': 'IrregularVerbAugmentedStem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stem': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Tense']"}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Verb']"})
        },
        u'drills.irregularverbform': {
            'Meta': {'object_name': 'IrregularVerbForm'},
            'form': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Mood']"}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Number']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Person']"}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Tense']"}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Verb']"}),
            'voice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Voice']"})
        },
        u'drills.irregularverbstem': {
            'Meta': {'object_name': 'IrregularVerbStem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Mood']"}),
            'stem': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Tense']"}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Verb']"}),
            'voice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Voice']"})
        },
        u'drills.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'drills.log': {
            'Meta': {'object_name': 'Log'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logfile': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'drills.longpenult': {
            'Meta': {'object_name': 'LongPenult'},
            'declinable': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['drills.DeclinableWord']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'drills.mood': {
            'Meta': {'object_name': 'Mood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.number': {
            'Meta': {'object_name': 'Number'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.tense': {
            'Meta': {'object_name': 'Tense'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.verb': {
            'Meta': {'object_name': 'Verb'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Conjugation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['drills.Word']", 'unique': 'True'}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.verbtensewithnopassive': {
            'Meta': {'object_name': 'VerbTenseWithNoPassive'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Tense']"}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Verb']"})
        },
        u'drills.vocabreviewresult': {
            'Meta': {'object_name': 'VocabReviewResult'},
            'correct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory_index': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Word']"}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.voice': {
            'Meta': {'object_name': 'Voice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'drills.word': {
            'Meta': {'object_name': 'Word'},
            'date_entered': ('django.db.models.fields.DateTimeField', [], {}),
            'definition': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_reviewed': ('django.db.models.fields.DateTimeField', [], {}),
            'last_wrong': ('django.db.models.fields.DateTimeField', [], {}),
            'memory_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'next_review': ('django.db.models.fields.DateTimeField', [], {}),
            'review_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['drills.Tag']", 'symmetrical': 'False'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wordlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.WordList']"})
        },
        u'drills.wordlist': {
            'Meta': {'object_name': 'WordList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drills.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['drills']