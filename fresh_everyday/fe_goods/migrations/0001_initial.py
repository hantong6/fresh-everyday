# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateGory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('weight', models.IntegerField()),
                ('abstract', models.CharField(default=b'', max_length=100)),
                ('detail', models.CharField(default=b'', max_length=1000)),
                ('category', models.ForeignKey(to='fe_goods.CateGory')),
            ],
        ),
    ]
