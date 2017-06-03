# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateGory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to=b'goods')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isdelete', models.BooleanField(default=False)),
                ('weight', models.CharField(default=b'500g', max_length=20)),
                ('click', models.IntegerField()),
                ('abstract', models.CharField(default=b'', max_length=200)),
                ('store', models.IntegerField()),
                ('detail', tinymce.models.HTMLField()),
                ('category', models.ForeignKey(to='fe_goods.CateGory')),
            ],
        ),
    ]
