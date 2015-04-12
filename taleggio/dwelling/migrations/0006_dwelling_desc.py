# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0005_remove_dwelling_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwelling',
            name='desc',
            field=models.CharField(default=b'Description', max_length=500),
        ),
    ]
