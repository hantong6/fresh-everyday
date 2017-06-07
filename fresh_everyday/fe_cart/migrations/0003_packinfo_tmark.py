# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fe_cart', '0002_packinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='packinfo',
            name='tmark',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 11, 35, 14, 143392, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
