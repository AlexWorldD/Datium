from comments.models import Comment, CommentsTable
from django.contrib.auth.models import User
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    table = serializers.PrimaryKeyRelatedField(queryset=CommentsTable.objects.all())

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

class CommentsTableObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.all()[0].id