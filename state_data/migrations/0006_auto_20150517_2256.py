# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0005_auto_20150517_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='color',
            field=models.CharField(null=True, max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='fact',
            field=models.ForeignKey(to='state_data.Fact'),
            preserve_default=True,
        ),
    ]
