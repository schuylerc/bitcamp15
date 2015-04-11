# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_review_usercreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlordreview',
            name='Landlord',
            field=models.ForeignKey(related_name='Landlord', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='UserCreated',
            field=models.ForeignKey(related_name='UserCreated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tenantreview',
            name='Tenant',
            field=models.ForeignKey(related_name='Tenant', to=settings.AUTH_USER_MODEL),
        ),
    ]
