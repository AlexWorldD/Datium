from comments.models import Comment, CommentsTable
from users.serializers import UserSerializer
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'table')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class CommentsTableSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsTable
        fields = ('id', 'comments')