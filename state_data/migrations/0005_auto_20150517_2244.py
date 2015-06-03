# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0004_auto_20150516_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='available_options',
        ),
        migrations.AddField(
            model_name='option',
            name='fact',
            field=models.ForeignKey(null=True, to='state_data.Fact'),
            preserve_default=True,
        ),
    ]
