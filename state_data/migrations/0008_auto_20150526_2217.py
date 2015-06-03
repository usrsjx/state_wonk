# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state_data', '0007_auto_20150517_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('label',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fact',
            name='details',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fact',
            name='sources',
            field=models.ManyToManyField(to='state_data.Source'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='statefact',
            name='sources',
            field=models.ManyToManyField(to='state_data.Source'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statefact',
            name='details',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
