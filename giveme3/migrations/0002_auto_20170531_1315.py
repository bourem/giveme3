# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-31 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveme3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='pluses',
            new_name='traits',
        ),
        migrations.AddField(
            model_name='votedtrait',
            name='plusminus',
            field=models.CharField(choices=[('+', 'Plus'), ('-', 'Minus'), ('z', 'Zero')], default='z', max_length=1),
        ),
    ]
