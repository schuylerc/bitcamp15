# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20150411_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='UserCreated',
            new_name='userCreated',
        ),
    ]
