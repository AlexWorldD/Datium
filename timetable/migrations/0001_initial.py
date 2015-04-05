# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0002_auto_20150405_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('lesson_type', models.IntegerField(choices=[(0, ''), (1, 'Практика'), (2, 'Лекция'), (3, 'Семинар')])),
                ('day', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')])),
                ('class_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LessonInTimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('lesson', models.ForeignKey(to='timetable.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('what_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('student_group', models.ForeignKey(to='student_groups.StudentGroup')),
            ],
        ),
        migrations.AddField(
            model_name='lessonintimetable',
            name='timetable',
            field=models.ForeignKey(to='timetable.Timetable'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(to='timetable.Subject'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(to='timetable.Teacher'),
        ),
        migrations.AddField(
            model_name='homework',
            name='deadline',
            field=models.ForeignKey(to='timetable.LessonInTimeTable'),
        ),
    ]
