# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0006_auto_20150412_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dwelling',
            name='apartment_number',
        ),
    ]
