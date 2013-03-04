from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def my_courses_view(request):
    return render(request, "my_courses.html")

def course_item_view(request):
    return render(request, "course_item.html")

