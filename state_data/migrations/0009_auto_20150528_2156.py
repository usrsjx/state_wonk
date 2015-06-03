# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0008_auto_20150526_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='sources',
            field=models.ManyToManyField(null=True, to='state_data.Source'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statefact',
            name='sources',
            field=models.ManyToManyField(null=True, to='state_data.Source'),
            preserve_default=True,
        ),
    ]
