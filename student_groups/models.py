#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from comments.models import CommentsTable


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey('StudentGroup')
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username


class StudentGroup(models.Model):
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
