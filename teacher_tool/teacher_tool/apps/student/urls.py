from django.conf.urls import patterns, url


urlpatterns = patterns('teacher_tool.apps.student.views',
    url(r'^$', 'groups_view', name='groups_list'),
    url(r'^(?P<id>\d+)/$', 'group_item_view', name='group_item'),
)
