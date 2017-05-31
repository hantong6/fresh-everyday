# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('addressee', models.CharField(default=b'', max_length=50)),
                ('telephone', models.CharField(default=b'', max_length=20)),
                ('postcode', models.CharField(default=b'', max_length=20)),
                ('address', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]
