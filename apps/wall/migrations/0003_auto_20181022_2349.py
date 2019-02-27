# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20181022_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messages',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall.Message'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='wall.User'),
        ),
    ]
