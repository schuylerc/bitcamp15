# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_auto_20150411_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dwellingreview',
            old_name='Dwelling',
            new_name='dwelling',
        ),
        migrations.RenameField(
            model_name='landlordreview',
            old_name='Landlord',
            new_name='landlord',
        ),
        migrations.RenameField(
            model_name='tenantreview',
            old_name='Tenant',
            new_name='tenant',
        ),
    ]
