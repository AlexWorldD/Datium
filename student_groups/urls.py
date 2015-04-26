from django.conf.urls import patterns, include, url
from student_groups.views import StudentGroupDetailAPIView, StudentGroupListAPIView, DocumentCreateAPIView,\
    DocumentListAPIView, DocumentDetailAPIView

urlpatterns = patterns('',
                       url(r'^groups/?$', StudentGroupListAPIView.as_view(), name="group-list-create"),
                       url(r'^groups/(?P<pk>[0-9]+)/?$', StudentGroupDetailAPIView.as_view(), name="group-detail"),
                       url(r'^documents/?$', DocumentListAPIView.as_view(), name="document-list"),
                       url(r'^documents/(?P<pk>[0-9]+)/?$', DocumentDetailAPIView.as_view(), name="document-list"),
                       url(r'^documents/upload_document/?$', DocumentCreateAPIView.as_view(), name="document-create"),
                       )