from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# from student_groups.models import Student
# import student_groups.models

# Create your models here.


class CommentsTable(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True)
    object_id = models.PositiveIntegerField(blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        unique_together   = ('content_type', 'object_id')


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    table = models.ForeignKey(CommentsTable, related_name='comments')

