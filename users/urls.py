from django.conf.urls import patterns, url
from users.views import UserListCreateAPIView, UserDetailAPIView, UserDetailByIDAPIView, UserAvatarUploadAPIView,\
    UserAvatarUploadByIDAPIView

urlpatterns = patterns('',
       url(r'^users/?$', UserListCreateAPIView.as_view()),
       url(r'^users/id/(?P<pk>[0-9]+)/?$', UserDetailByIDAPIView.as_view()),
       url(r'^users/(?P<username>\w+)/?$', UserDetailAPIView.as_view()),
       url(r'^users/id/(?P<pk>[0-9]+)/upload_avatar/?$', UserAvatarUploadByIDAPIView.as_view()),
       url(r'^users/(?P<username>\w+)/upload_avatar/?$', UserAvatarUploadAPIView.as_view()),
)