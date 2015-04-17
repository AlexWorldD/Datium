from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

# from authentication.views import UserListCreateAPIView, StudentListCreateAPIView
from authentication.views import UserListCreateAPIView, UserDetailAPIView
from timetable.views import SubjectDetailAPIView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'api/v1/users/', UserListCreateAPIView.as_view()),
                       url(r'api/v1/users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view()),
                       url(r'api/v1/', include('timetable.urls')),
                       url(r'^.*$', TemplateView.as_view(template_name='index.html')),

                       )
