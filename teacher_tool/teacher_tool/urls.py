from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'teacher_tool.views.index', name='index'),
    url(r'^my_courses/$', 'teacher_tool.views.my_courses_view', name='my_courses_list'),
    url(r'^my_courses/course_item/$', 'teacher_tool.views.course_item_view', name='course_list'),
    url(r'^groups/$', 'teacher_tool.views.groups_view', name='groups_list'),


    # url(r'^teacher_tool/', include('teacher_tool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
