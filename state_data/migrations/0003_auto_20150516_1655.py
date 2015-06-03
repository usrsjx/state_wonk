# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0002_auto_20150513_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='statefact',
            name='details',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
