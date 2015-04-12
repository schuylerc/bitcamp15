# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0002_auto_20150411_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dwelling',
            old_name='dwellingType',
            new_name='dwelling_type',
        ),
    ]
