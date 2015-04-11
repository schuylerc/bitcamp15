# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20150411_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlordreview',
            name='Landlord',
            field=models.ForeignKey(related_name='Landlord', default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tenantreview',
            name='Tenant',
            field=models.ForeignKey(related_name='Tenant', default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
