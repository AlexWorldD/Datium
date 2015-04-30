from django.conf.urls import patterns, include, url
from student_groups.views import StudentGroupDetailAPIView, StudentGroupListAPIView, DocumentListCreateAPIView,\
    DocumentRetrieveUpdateDestroyAPIView, NewsListCreateAPIView, NewsRetrieveUpdateDestroyAPIView

urlpatterns = patterns('',
                       url(r'^groups/?$', StudentGroupListAPIView.as_view(), name="group-list-create"),
                       url(r'^groups/(?P<pk>[0-9]+)/?$', StudentGroupDetailAPIView.as_view(), name="group-detail"),
                       url(r'^documents/?$', DocumentListCreateAPIView.as_view(), name="document-list-create"),
                       url(r'^documents/(?P<pk>[0-9]+)/?$', DocumentRetrieveUpdateDestroyAPIView.as_view(), name="document-detail"),
                       url(r'^news/?$', NewsListCreateAPIView.as_view(), name="news-list-create"),
                       url(r'^news/(?P<pk>[0-9]+)/?$', NewsRetrieveUpdateDestroyAPIView.as_view(), name="news-detail"),
                       )