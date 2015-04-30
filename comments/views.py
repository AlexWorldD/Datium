from comments.models import Comment, CommentsTable
from comments.serializers import CommentSerializer, CommentsTableSerializer
from rest_framework import generics, permissions
from users.permissions import CanPostComments

# Create your views here.


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, CanPostComments)


class CommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, CanPostComments)


class CommentsTableDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentsTableSerializer
    queryset = CommentsTable.objects.all()
    permissions_classes = (permissions.IsAuthenticated, CanPostComments)


