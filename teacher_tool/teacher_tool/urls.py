from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'teacher_tool.views.index', name='index'),
    url(r'^my_courses/$', 'teacher_tool.views.my_courses_view', name='my_courses_list'),
    url(r'^my_courses/course_item/$', 'teacher_tool.views.course_item_view', name='course_item'),
    url(r'^student/(?P<id>\d+)/$', 'teacher_tool.apps.student.views.student_item_view', name='student_item'),
    url(r'^student/create/$', 'teacher_tool.apps.student.views.student_item_edit', name='student_create'),
    url(r'^student/(?P<id>\d+)/edit/$', 'teacher_tool.apps.student.views.student_item_edit', name='student_edit'),


    url(r'^groups/', include('teacher_tool.apps.student.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
