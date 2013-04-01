from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from teacher_tool.apps.student.models import Student, Group


@login_required
def group_item_view(request, id):
    # try:
    #     group = Group.objects.get(id=id)
    # except Group.DoesNotExist:
    #     raise Http404

    group = get_object_or_404(Group, id=id)


    students = Student.objects.filter(group=group)
    paginator = Paginator(students, 5)
    page = request.GET.get('page', 1)
    try:
        students = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        raise Http404

    return render(request, "group_item.html",
                  {'students': students,
                   'group': group})


@login_required
def groups_view(request):
    groups = Group.objects.all()
    return render(request, "groups.html",
                  {'groups': groups})


@login_required
def student_item_view(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "student_item.html",
                  {'student': student})


class StudentForm(ModelForm):

    class Meta:
        model = Student


@login_required
def student_item_edit(request, id=None):
    if not request.user.is_superuser:
        return redirect(reverse("login") + "?next=%s" % request.META['PATH_INFO'])

    if id is not None:
        student = get_object_or_404(Student, id=id)
    else:
        student = None

    if request.GET:
        form = StudentForm(request.GET, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect(reverse('student_item', args=[student.id]))
    else:
        form = StudentForm(instance=student)

    return render(request, "student_edit_item.html",
                  {'student': student, 'form': form})

# def student_item_edit(request, id=None):
#     if id is not None:
#         print request.GET

#         student = get_object_or_404(Student, id=id)
#         if request.GET:
#             if 'first_name' in request.GET:
#                 student.first_name = request.GET['first_name']
#             if 'last_name' in request.GET:
#                 student.last_name = request.GET['last_name']
#             student.save()

#     else:
#         group = Group.objects.all()[0]
#         student = Student()
#         student.group = group
#         student.first_name = "test"
#         student.last_name = "testovich2"
#         student.save()

#         return redirect(reverse('student_item', args=[student.id]))

#     return render(request, "student_edit_item.html",
#                   {'student': student})

