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

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^groups/', include('teacher_tool.apps.student.urls')),
    url(r'^course/', include('teacher_tool.apps.course.urls')),
    # url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^contact/$', 'teacher_tool.views.contact', name="contact_page"),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^pages(?P<url>.*)$', 'flatpage', name='flatpage'),
)