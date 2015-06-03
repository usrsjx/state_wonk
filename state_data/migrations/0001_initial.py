# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=3, choices=[('pct', 'Percentage'), ('nbr', 'Number'), ('opt', 'Multiple Options')], default='opt')),
                ('source_label', models.CharField(max_length=30, blank=True)),
                ('source_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ('label',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('abbr',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StateFact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=255)),
                ('source_label', models.CharField(max_length=30, blank=True)),
                ('source_url', models.URLField(blank=True)),
                ('pct', models.FloatField(blank=True)),
                ('nbr', models.IntegerField(blank=True)),
                ('fact', models.ForeignKey(to='state_data.Fact')),
                ('opt', models.ForeignKey(to='state_data.Option', blank=True)),
                ('state', models.ForeignKey(to='state_data.State')),
            ],
            options={
                'ordering': ('fact', 'state'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fact',
            name='available_options',
            field=models.ManyToManyField(to='state_data.Option'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fact',
            name='category',
            field=models.ForeignKey(to='state_data.Category'),
            preserve_default=True,
        ),
    ]
