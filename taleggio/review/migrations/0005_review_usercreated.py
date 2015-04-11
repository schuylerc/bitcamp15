# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0004_remove_review_usercreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='UserCreated',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
