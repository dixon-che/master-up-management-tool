from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)