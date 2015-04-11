# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0002_auto_20150411_1753'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DwellingReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='review.Review')),
                ('Dwelling', models.ForeignKey(to='dwelling.Dwelling')),
            ],
            bases=('review.review',),
        ),
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
