from django.conf.urls import patterns, url
from users.views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = patterns('',
       url(r'^users/$', UserListCreateAPIView.as_view()),
       url(r'^users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view()),
)