# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdgqpt', '0012_auto_20160915_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='caozuopiao',
            name='beizhu',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
    ]
