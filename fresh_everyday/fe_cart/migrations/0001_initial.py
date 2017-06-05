# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fe_goods', '0001_initial'),
        ('fe_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('isdelete', models.BooleanField(default=False)),
                ('good', models.ForeignKey(to='fe_goods.GoodInfo')),
                ('user', models.ForeignKey(to='fe_user.UserInfo')),
            ],
        ),
    ]
