# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20141209_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='has_preference',
            field=models.BooleanField(default=False, verbose_name=b'Has Submitted Preference'),
            preserve_default=True,
        ),
    ]
