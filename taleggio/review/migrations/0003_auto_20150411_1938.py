# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_auto_20150411_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandlordReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='review.Review')),
                ('Landlord', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('review.review',),
        ),
        migrations.CreateModel(
            name='TenantReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='review.Review')),
                ('Tenant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('review.review',),
        ),
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
    ]
