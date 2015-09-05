# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0015_auto_20150509_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('none', ''), ('practice', 'practice'), ('lection', 'lection'), ('seminar', 'seminar')], max_length=8),
        ),
    ]
