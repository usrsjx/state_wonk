# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0003_auto_20150516_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statefact',
            name='nbr',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statefact',
            name='opt',
            field=models.ForeignKey(blank=True, null=True, to='state_data.Option'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statefact',
            name='pct',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
