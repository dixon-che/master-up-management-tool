from django.db import models
from teacher_tool.apps.student.models import Student, Group


class Course(models.Model):
    group = models.OneToOneField(Group)
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class Lesson(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=30)
    description = models.TextField()
    home_work = models.TextField()
    video = models.URLField(max_length=255, blank=True, null=True)
    lecture = models.FileField(upload_to='lectures', blank=True, null=True)
    datetime = models.DateTimeField()


class StudentsResults(models.Model):
    lesson = models.ForeignKey(Lesson)
    student = models.ForeignKey(Student)
    attendance = models.BooleanField(default=True)
    home_work_done = models.BooleanField(default=True)
    home_work_note = models.TextField()

    class Meta:
        unique_together = (("lesson", "student"), )
