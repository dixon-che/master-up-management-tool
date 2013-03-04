from django.views.generic.simple import direct_to_template
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from teacher_tool.apps.student.models import Student, Group


def group_item_view(request, id):
    # try:
    #     group = Group.objects.get(id=id)
    # except Group.DoesNotExist:
    #     raise Http404

    group = get_object_or_404(Group, id=id)

    students = Student.objects.filter(group=group)
    return render(request, "group_item.html",
                  {'students': students,
                   'group': group})


def groups_view(request):
    groups = Group.objects.all()
    return render(request, "groups.html",
                  {'groups': groups})


def student_item_view(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "student_item.html",
                  {'student': student})
