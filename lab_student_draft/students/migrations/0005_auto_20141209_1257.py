# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20141209_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name': 'Batch', 'verbose_name_plural': 'Batches'},
        ),
        migrations.AddField(
            model_name='batch',
            name='maximum_groups',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batch',
            name='minimum_groups',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
