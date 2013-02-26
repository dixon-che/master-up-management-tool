from django.views.generic.simple import direct_to_template
from django.shortcuts import render

from teacher_tool.apps.student.models import Student


def group_item_view(request):
    students = Student.objects.all()
    return render(request, "group_item.html",
                  {'students': students})
