#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from student_groups.models import StudentGroup, Document

# Create your models here.

class LessonType(models.Model):

    what_type = models.CharField(max_length = 200)

class Teacher(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    dept = models.CharField(max_length = 200)

class Subject(models.Model):
    # предмет (Вычислительная математика, Физика и т.п., без типа)
    name = models.CharField(max_length = 200)
    
class Lesson(models.Model):
    # занятие (Вычислительная математика, практика; Физика, лекция и т.п)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    
    NONE = 0
    PRACTICE = 1
    LECTION = 2
    SEMINAR = 3
    LESSON_TYPE_CHOICES = (
        (NONE, ''),
        (PRACTICE, 'Практика'),
        (LECTION, 'Лекция'),
        (SEMINAR, 'Семинар'),
    )
    lesson_type = models.IntegerField(choices = LESSON_TYPE_CHOICES)
    
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEKDAY = (
        (MONDAY, 'Понедельник'),
        (TUESDAY, 'Вторник'),
        (WEDNESDAY, 'Среда'),
        (THURSDAY, 'Четверг'),
        (FRIDAY, 'Пятница'),
        (SATURDAY, 'Суббота'),
    )
    day = models.IntegerField(choices = WEEKDAY)
    class_number = models.IntegerField() # первая пара, вторая пара… 
    
class LessonInTimeTable(models.Model):
    # конкретное занятие (лекция по физике 5 марта)
    lesson = models.ForeignKey(Lesson)
    datetime = models.DateTimeField()
    timetable = models.ForeignKey('Timetable')
    
class Homework(models.Model):
    text = models.TextField()
    deadline = models.ForeignKey(LessonInTimeTable)
    documents = models.ManyToManyField(Document)

class Timetable(models.Model):
    student_group = models.ForeignKey(StudentGroup)
    
