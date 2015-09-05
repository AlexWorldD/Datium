#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from student_groups.models import StudentGroup, Document
from comments.models import CommentsTable
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,)
    patronymic = models.CharField(max_length=200, blank=True)   #отчество
    department = models.ForeignKey('Department', related_name='department', default=0)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    cabinet = models.CharField(max_length=20, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=200)


class Subject(models.Model):
    # предмет (Вычислительная математика, Физика и т.п., без типа)
    name = models.CharField(max_length=200, unique=True)


class Lesson(models.Model):
    # занятие (Вычислительная математика, практика; Физика, лекция и т.п)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    group = models.ForeignKey(StudentGroup)
    semester = models.IntegerField()

    NONE = 'none'
    PRACTICE = 'practice'
    LECTION = 'lection'
    SEMINAR = 'seminar'
    LESSON_TYPE_CHOICES = (
        (NONE, ''),
        (PRACTICE, 'practice'),
        (LECTION, 'lection'),
        (SEMINAR, 'seminar'),
    )
    lesson_type = models.CharField(max_length=8,  choices=LESSON_TYPE_CHOICES)

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEKDAY = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
    )
    day = models.IntegerField(choices=WEEKDAY)
    class_number = models.IntegerField()  # первая пара, вторая пара…
    class Meta:
        unique_together   = ('group', 'semester', 'day', 'class_number')


class LessonInTimeTable(models.Model):
    # конкретное занятие (лекция по физике 5 марта)
    lesson = models.ForeignKey(Lesson)
    start = models.DateTimeField()
    end = models.DateTimeField()
    day = models.ForeignKey('DayInTimetable')


class Homework(models.Model):
    text = models.TextField()
    deadline = models.ForeignKey(LessonInTimeTable)
    documents = models.ManyToManyField(Document)
    user = models.ForeignKey(User)
    comments = GenericRelation(CommentsTable, related_query_name='homework')

class DayInTimetable(models.Model):
    date = models.DateField()
    weekday = models.IntegerField(choices=Lesson.WEEKDAY)
    week = models.ForeignKey('WeekInTimetable')

class WeekInTimetable(models.Model):
    week_number = models.IntegerField()
    timetable = models.ForeignKey('Timetable')


class Timetable(models.Model):
    group = models.ForeignKey(StudentGroup)
    semester = models.IntegerField()
    class Meta:
        unique_together   = ('group', 'semester')