# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0005_auto_20150411_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=b'/static/images/avatars/default_avatar.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
