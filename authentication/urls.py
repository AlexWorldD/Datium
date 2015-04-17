from django.conf.urls import patterns, url

urlpatterns = patterns('',
       url(r'^auth/login/$', 'rest_framework_jwt.views.obtain_jwt_token'),
)