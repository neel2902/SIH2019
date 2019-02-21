# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-21 10:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('emergency_phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('long', models.DecimalField(decimal_places=6, max_digits=10)),
                ('is_safe', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
