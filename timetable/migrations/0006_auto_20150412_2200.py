# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20150412_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='dept',
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(related_name='department', default=0, to='timetable.Department'),
        ),
    ]
