from django.db import models


class Group(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Student(models.Model):

    group = models.ForeignKey(Group)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    skype = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)
