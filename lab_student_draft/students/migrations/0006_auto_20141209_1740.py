# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20141209_1257'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grouppreference',
            unique_together=set([('student_group', 'lab', 'preference')]),
        ),
    ]
