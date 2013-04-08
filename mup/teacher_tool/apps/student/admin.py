from django.contrib import admin
from teacher_tool.apps.student.models import Student, Group


admin.site.register(Student)
admin.site.register(Group)