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
            name='apartment_number',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='dwelling_type',
            field=models.CharField(blank=True, max_length=2, choices=[(b'TH', b'Townhouse'), (b'A', b'Apartment'), (b'H', b'House')]),
        ),
    ]
