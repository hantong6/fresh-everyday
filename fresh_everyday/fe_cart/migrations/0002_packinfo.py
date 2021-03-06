# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fe_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField()),
                ('isdelete', models.BooleanField(default=False)),
                ('order', models.ForeignKey(to='fe_cart.OrderInfo')),
            ],
        ),
    ]
