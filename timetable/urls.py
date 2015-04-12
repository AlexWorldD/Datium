from django.conf.urls import patterns, include, url
from timetable.views import SubjectListAPIView, SubjectDetailAPIView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^subjects/$', SubjectListAPIView.as_view()),
    url(r'^subjects/(?P<pk>[0-9]+)/$', SubjectDetailAPIView.as_view(), name="subject-detail"),

)
