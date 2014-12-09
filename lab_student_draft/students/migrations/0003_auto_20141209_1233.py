# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141209_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentgroup',
            new_name='student_group',
        ),
        migrations.AlterUniqueTogether(
            name='grouppreference',
            unique_together=set([('student_group', 'lab')]),
        ),
        migrations.AlterUniqueTogether(
            name='selection',
            unique_together=set([('lab', 'student_group')]),
        ),
    ]
