from django.views.generic.simple import direct_to_template


def index(request):
    return direct_to_template(request, "index.html")

def my_courses_view(request):
    return direct_to_template(request, "my_courses.html")

def course_item_view(request):
    return direct_to_template(request, "course_item.html")

