from django.conf.urls import patterns, include, url
from comments.views import CommentsTableDetailAPIView, CommentDetailAPIView, CommentCreateAPIView

urlpatterns = patterns('',
                       url(r'^comments/?$', CommentCreateAPIView.as_view(), name="comment-create"),
                       url(r'^comments/(?P<pk>[0-9]+)/?$', CommentDetailAPIView.as_view(), name="comment-detail"),
                       url(r'^commentstables/(?P<pk>[0-9]+)/?$', CommentsTableDetailAPIView.as_view(), name="commentstable-detail"),
                       )
