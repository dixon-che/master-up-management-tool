from django.http import HttpResponse
from django.views.generic.simple import direct_to_template


def index(request):
    return direct_to_template(request, "index.html")


def my_cources_view(request):
    return direct_to_template(request, "my_cources.html")


def groups_view(request):
    return direct_to_template(request, "groups.html")

