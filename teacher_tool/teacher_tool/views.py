from django.http import HttpResponse
from django.views.generic.simple import direct_to_template


def index(request):
    return direct_to_template(request, "index.html")

def my_courses_view(request):
    return direct_to_template(request, "my_courses.html")

def course_item_view(request):
    return direct_to_template(request, "course_item.html")

def groups_view(request):
    return direct_to_template(request, "groups.html")

def group_item_view(request):
    return direct_to_template(request, "group_item.html")

def student_item_view(request):
    return direct_to_template(request, "student_item.html")

