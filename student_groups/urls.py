from django.conf.urls import patterns, include, url
from student_groups.views import StudentGroupDetailAPIView, StudentGroupListAPIView

urlpatterns = patterns('',
                       url(r'^groups/$', StudentGroupListAPIView.as_view(), name="group-list-create"),
                       url(r'^groups/(?P<pk>[0-9]+)/$', StudentGroupDetailAPIView.as_view(), name="group-detail"),
                       )