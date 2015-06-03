# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0006_auto_20150517_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='color',
            field=models.CharField(max_length=7),
            preserve_default=True,
        ),
    ]
