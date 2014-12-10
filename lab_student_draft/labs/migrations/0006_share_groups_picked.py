# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0005_lab_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='groups_picked',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
