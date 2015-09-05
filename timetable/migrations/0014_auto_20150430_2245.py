# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='cabinet',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='patronymic',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
