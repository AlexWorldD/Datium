# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0003_auto_20150409_2105'),
        ('timetable', '0002_auto_20150407_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='documents',
            field=models.ManyToManyField(to='student_groups.Document'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.IntegerField(choices=[(0, ''), (1, 'Практика'), (2, 'Лекция'), (3, 'Семинар')]),
        ),
    ]
