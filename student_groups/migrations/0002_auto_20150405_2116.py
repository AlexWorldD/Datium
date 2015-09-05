# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('student_groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='comments',
            field=models.OneToOneField(to='comments.CommentsTable', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.OneToOneField(to='comments.CommentsTable', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(max_length=200),
        ),
    ]
