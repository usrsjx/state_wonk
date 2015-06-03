# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='source_label',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='label',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statefact',
            name='source_label',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
