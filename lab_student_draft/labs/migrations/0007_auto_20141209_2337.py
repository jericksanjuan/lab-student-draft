# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0006_share_groups_picked'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='desired_groups',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lab',
            name='groups_picked',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lab',
            name='slots_taken',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
