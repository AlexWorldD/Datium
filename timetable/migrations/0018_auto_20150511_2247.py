# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0017_auto_20150510_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayInTimetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
            ],
        ),
        migrations.CreateModel(
            name='WeekInTimetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('week_number', models.IntegerField()),
                ('timetable', models.ForeignKey(to='timetable.Timetable')),
            ],
        ),
        migrations.RemoveField(
            model_name='lessonintimetable',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='lessonintimetable',
            name='timetable',
        ),
        migrations.AddField(
            model_name='lessonintimetable',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 47, 26, 318084, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonintimetable',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 47, 38, 881803, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayintimetable',
            name='week',
            field=models.ForeignKey(to='timetable.WeekInTimetable'),
        ),
        migrations.AddField(
            model_name='lessonintimetable',
            name='day',
            field=models.ForeignKey(to='timetable.DayInTimetable', default=1),
            preserve_default=False,
        ),
    ]
