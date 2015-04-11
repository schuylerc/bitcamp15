# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dwelling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('dwellingType', models.CharField(max_length=2, choices=[(b'TH', b'Townhouse'), (b'A', b'Apartment'), (b'H', b'House')])),
                ('address', models.ForeignKey(to='dwelling.Address')),
            ],
        ),
    ]
