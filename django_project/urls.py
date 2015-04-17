from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/v1/', include('authentication.urls')),
                       url(r'api/v1/', include('timetable.urls')),
                       url(r'api/v1/', include('users.urls')),
                       url(r'^.*$', TemplateView.as_view(template_name='index.html')),

                       )
