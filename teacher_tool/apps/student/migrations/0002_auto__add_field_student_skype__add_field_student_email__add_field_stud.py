# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.skype'
        db.add_column(u'student_student', 'skype',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.email'
        db.add_column(u'student_student', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.github'
        db.add_column(u'student_student', 'github',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.phone'
        db.add_column(u'student_student', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.skype'
        db.delete_column(u'student_student', 'skype')

        # Deleting field 'Student.email'
        db.delete_column(u'student_student', 'email')

        # Deleting field 'Student.github'
        db.delete_column(u'student_student', 'github')

        # Deleting field 'Student.phone'
        db.delete_column(u'student_student', 'phone')


    models = {
        u'student.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'student.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['student']