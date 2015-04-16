# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0008_auto_20150413_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='student_groups.StudentGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
