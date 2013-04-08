# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'course_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['student.Group'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'course', ['Course'])

        # Adding model 'Lesson'
        db.create_table(u'course_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('home_work', self.gf('django.db.models.fields.TextField')()),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('lecture', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'course', ['Lesson'])

        # Adding model 'StudentsResults'
        db.create_table(u'course_studentsresults', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Lesson'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student.Student'])),
            ('attendance', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('home_work_done', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('home_work_note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'course', ['StudentsResults'])

        # Adding unique constraint on 'StudentsResults', fields ['lesson', 'student']
        db.create_unique(u'course_studentsresults', ['lesson_id', 'student_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'StudentsResults', fields ['lesson', 'student']
        db.delete_unique(u'course_studentsresults', ['lesson_id', 'student_id'])

        # Deleting model 'Course'
        db.delete_table(u'course_course')

        # Deleting model 'Lesson'
        db.delete_table(u'course_lesson')

        # Deleting model 'StudentsResults'
        db.delete_table(u'course_studentsresults')


    models = {
        u'course.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['student.Group']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'course.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.Course']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'home_work': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'course.studentsresults': {
            'Meta': {'unique_together': "(('lesson', 'student'),)", 'object_name': 'StudentsResults'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_work_done': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_work_note': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.Lesson']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student.Student']"})
        },
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

    complete_apps = ['course']