from django.conf.urls import patterns, url


urlpatterns = patterns('teacher_tool.apps.course.views',
    url(r'^$', 'courses_view', name='courses_list'),
)