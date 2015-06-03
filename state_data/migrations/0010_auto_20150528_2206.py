# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0009_auto_20150528_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='source_label',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='source_url',
        ),
        migrations.RemoveField(
            model_name='statefact',
            name='source_label',
        ),
        migrations.RemoveField(
            model_name='statefact',
            name='source_url',
        ),
        migrations.AlterField(
            model_name='source',
            name='label',
            field=models.CharField(null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
