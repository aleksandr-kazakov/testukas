# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Q', models.TextField()),
                ('A1', models.TextField()),
                ('A2', models.TextField()),
                ('A3', models.TextField()),
                ('A4', models.TextField()),
                ('A5', models.TextField()),
                ('A6', models.TextField()),
                ('QType', models.TextField()),
                ('RightAnswer', models.CharField(max_length=6)),
                ('Source', models.URLField()),
                ('Comment', models.TextField()),
            ],
        ),
    ]
