# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0019_auto_20150502_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hall',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
