#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from comments.models import CommentsTable
from django.templatetags.static import static

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, default=0)
    group = models.ForeignKey('StudentGroup')
    avatar = models.ImageField(default=static('images/avatars/default_avatar.png'))

    def __str__(self):
        return self.user.username


class StudentGroup(models.Model):
    class Meta:
        permissions = (
            ("view_timetable", "Can see timetable of the group"), # groups: 'registered', 'students', 'group admin'
            ("view_grouplist", "Can see the list of students in the group"), # groups: 'registered', 'students', 'group admin'
            ("view_news", "Can see news of the group"), # groups: 'students', 'group admin'
            ("view_homeworks", "Can see homeworks"), # groups: 'students', 'group admin'
            ("view_documents", "Can see documents"), # groups: 'students', 'group admin'
            ("add_and_edit_news", "Can add and edit news of the group"), # groups: 'group admin'
            ("add_and_edit_homeworks", "Can add and edit homeworks"), # groups: 'group admin'
            ("add_and_edit_documents", "Can add and edit documents"), # groups: 'group admin'
        )
    name = models.CharField(max_length = 200)
    study_year = models.IntegerField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(Student)
    group = models.ForeignKey(StudentGroup)
    tags = models.ManyToManyField('Tag')
    comments = models.OneToOneField(CommentsTable)
    documents = models.ManyToManyField('Document')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.SlugField(max_length = 200)


class Document(models.Model):
    file = models.FileField()
    name = models.CharField(max_length = 200)
    group = models.ForeignKey(StudentGroup)
    tags = models.ManyToManyField(Tag)
    comments = models.OneToOneField(CommentsTable)
