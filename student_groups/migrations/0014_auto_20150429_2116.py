# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import student_groups.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0013_auto_20150420_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=student_groups.models.group_documents_path),
        ),
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=b'/static/images/avatars/default_avatar.png', upload_to=b'avatars'),
        ),
    ]
