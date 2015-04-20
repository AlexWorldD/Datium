from comments.models import Comment, CommentsTable
from comments.serializers import CommentSerializer, CommentsTableSerializer
from rest_framework import generics, permissions

# Create your views here.


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class CommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class CommentsTableDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentsTableSerializer
    queryset = CommentsTable.objects.all()
    permissions_classes = (permissions.IsAuthenticated,)


