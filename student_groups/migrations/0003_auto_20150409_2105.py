# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0002_auto_20150405_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='documents',
            field=models.ManyToManyField(to='student_groups.Document'),
        ),
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
