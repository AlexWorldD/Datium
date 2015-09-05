# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0010_auto_20150416_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default=b'unknown', max_length=10),
        ),
    ]
