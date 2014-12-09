# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141209_1233'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='selection',
            unique_together=set([('lab', 'student_group', 'phase')]),
        ),
    ]
