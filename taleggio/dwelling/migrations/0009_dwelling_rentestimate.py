# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwelling',
            name='rentEstimate',
            field=models.IntegerField(default=1000),
        ),
    ]
