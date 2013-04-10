# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'drills_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('module_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'drills', ['Language'])

        # Adding model 'Declension'
        db.create_table(u'drills_declension', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Declension'])

        # Adding model 'DeclinableType'
        db.create_table(u'drills_declinabletype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['DeclinableType'])

        # Adding model 'Case'
        db.create_table(u'drills_case', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Case'])

        # Adding model 'Number'
        db.create_table(u'drills_number', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Number'])

        # Adding model 'Gender'
        db.create_table(u'drills_gender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Gender'])

        # Adding model 'Conjugation'
        db.create_table(u'drills_conjugation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Conjugation'])

        # Adding model 'Tense'
        db.create_table(u'drills_tense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Tense'])

        # Adding model 'Voice'
        db.create_table(u'drills_voice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Voice'])

        # Adding model 'Mood'
        db.create_table(u'drills_mood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Mood'])

        # Adding model 'Person'
        db.create_table(u'drills_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['Person'])

        # Adding model 'WordList'
        db.create_table(u'drills_wordlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Language'])),
        ))
        db.send_create_signal(u'drills', ['WordList'])

        # Adding model 'Tag'
        db.create_table(u'drills_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
        ))
        db.send_create_signal(u'drills', ['Tag'])

        # Adding model 'Word'
        db.create_table(u'drills_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('definition', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('date_entered', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_reviewed', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_wrong', self.gf('django.db.models.fields.DateTimeField')()),
            ('memory_index', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('next_review', self.gf('django.db.models.fields.DateTimeField')()),
            ('review_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'drills', ['Word'])

        # Adding M2M table for field tags on 'Word'
        db.create_table(u'drills_word_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('word', models.ForeignKey(orm[u'drills.word'], null=False)),
            ('tag', models.ForeignKey(orm[u'drills.tag'], null=False))
        ))
        db.create_unique(u'drills_word_tags', ['word_id', 'tag_id'])

        # Adding model 'Verb'
        db.create_table(u'drills_verb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['drills.Word'], unique=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Conjugation'])),
        ))
        db.send_create_signal(u'drills', ['Verb'])

        # Adding model 'IrregularVerbForm'
        db.create_table(u'drills_irregularverbform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Verb'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Person'])),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Number'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Tense'])),
            ('mood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Mood'])),
            ('voice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Voice'])),
            ('form', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'drills', ['IrregularVerbForm'])

        # Adding model 'IrregularVerbStem'
        db.create_table(u'drills_irregularverbstem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Verb'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Tense'])),
            ('mood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Mood'])),
            ('voice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Voice'])),
            ('stem', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'drills', ['IrregularVerbStem'])

        # Adding model 'IrregularVerbAugmentedStem'
        db.create_table(u'drills_irregularverbaugmentedstem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Verb'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Tense'])),
            ('stem', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'drills', ['IrregularVerbAugmentedStem'])

        # Adding model 'VerbTenseWithNoPassive'
        db.create_table(u'drills_verbtensewithnopassive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Verb'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Tense'])),
        ))
        db.send_create_signal(u'drills', ['VerbTenseWithNoPassive'])

        # Adding model 'DeclinableWord'
        db.create_table(u'drills_declinableword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['drills.Word'], unique=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('declension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Declension'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.DeclinableType'])),
        ))
        db.send_create_signal(u'drills', ['DeclinableWord'])

        # Adding model 'IrregularDeclinableForm'
        db.create_table(u'drills_irregulardeclinableform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declinable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.DeclinableWord'])),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Gender'])),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Number'])),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Case'])),
            ('form', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'drills', ['IrregularDeclinableForm'])

        # Adding model 'LongPenult'
        db.create_table(u'drills_longpenult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declinable', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['drills.DeclinableWord'], unique=True)),
        ))
        db.send_create_signal(u'drills', ['LongPenult'])

        # Adding model 'Log'
        db.create_table(u'drills_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('logfile', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'drills', ['Log'])

        # Adding model 'VocabReviewResult'
        db.create_table(u'drills_vocabreviewresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Word'])),
            ('memory_index', self.gf('django.db.models.fields.IntegerField')()),
            ('correct', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'drills', ['VocabReviewResult'])

        # Adding model 'ConjugationDrillResult'
        db.create_table(u'drills_conjugationdrillresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Verb'])),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Conjugation'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Person'])),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Number'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Tense'])),
            ('mood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Mood'])),
            ('voice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Voice'])),
            ('correct', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'drills', ['ConjugationDrillResult'])

        # Adding model 'DeclensionDrillResult'
        db.create_table(u'drills_declensiondrillresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wordlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.WordList'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.DeclinableWord'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.DeclinableType'])),
            ('declension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Declension'])),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Gender'])),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Number'])),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drills.Case'])),
            ('correct', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'drills', ['DeclensionDrillResult'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'drills_language')

        # Deleting model 'Declension'
        db.delete_table(u'drills_declension')

        # Deleting model 'DeclinableType'
        db.delete_table(u'drills_declinabletype')

        # Deleting model 'Case'
        db.delete_table(u'drills_case')

        # Deleting model 'Number'
        db.delete_table(u'drills_number')

        # Deleting model 'Gender'
        db.delete_table(u'drills_gender')

        # Deleting model 'Conjugation'
        db.delete_table(u'drills_conjugation')

        # Deleting model 'Tense'
        db.delete_table(u'drills_tense')

        # Deleting model 'Voice'
        db.delete_table(u'drills_voice')

        # Deleting model 'Mood'
        db.delete_table(u'drills_mood')

        # Deleting model 'Person'
        db.delete_table(u'drills_person')

        # Deleting model 'WordList'
        db.delete_table(u'drills_wordlist')

        # Deleting model 'Tag'
        db.delete_table(u'drills_tag')

        # Deleting model 'Word'
        db.delete_table(u'drills_word')

        # Removing M2M table for field tags on 'Word'
        db.delete_table('drills_word_tags')

        # Deleting model 'Verb'
        db.delete_table(u'drills_verb')

        # Deleting model 'IrregularVerbForm'
        db.delete_table(u'drills_irregularverbform')

        # Deleting model 'IrregularVerbStem'
        db.delete_table(u'drills_irregularverbstem')

        # Deleting model 'IrregularVerbAugmentedStem'
        db.delete_table(u'drills_irregularverbaugmentedstem')

        # Deleting model 'VerbTenseWithNoPassive'
        db.delete_table(u'drills_verbtensewithnopassive')

        # Deleting model 'DeclinableWord'
        db.delete_table(u'drills_declinableword')

        # Deleting model 'IrregularDeclinableForm'
        db.delete_table(u'drills_irregulardeclinableform')

        # Deleting model 'LongPenult'
        db.delete_table(u'drills_longpenult')

        # Deleting model 'Log'
        db.delete_table(u'drills_log')

        # Deleting model 'VocabReviewResult'
        db.delete_table(u'drills_vocabreviewresult')

        # Deleting model 'ConjugationDrillResult'
        db.delete_table(u'drills_conjugationdrillresult')

        # Deleting model 'DeclensionDrillResult'
        db.delete_table(u'drills_declensiondrillresult')


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