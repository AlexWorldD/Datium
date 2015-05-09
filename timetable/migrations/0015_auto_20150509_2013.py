# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0021_auto_20150509_2013'),
        ('timetable', '0014_auto_20150430_2245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LessonType',
        ),
        migrations.AddField(
            model_name='lesson',
            name='group',
            field=models.ForeignKey(to='student_groups.StudentGroup', default=None),
            preserve_default=False,
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
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
