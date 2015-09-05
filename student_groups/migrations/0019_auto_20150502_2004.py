# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0018_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='hall',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
