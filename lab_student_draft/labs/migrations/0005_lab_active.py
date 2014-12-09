# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0004_auto_20141209_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
