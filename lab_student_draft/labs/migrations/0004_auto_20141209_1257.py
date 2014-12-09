# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20141209_1257'),
        ('labs', '0003_auto_20141209_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slots_taken', models.IntegerField(default=0)),
                ('desired_groups', models.IntegerField(default=1)),
                ('batch', models.ForeignKey(to='students.Batch')),
                ('lab', models.ForeignKey(to='labs.Lab')),
            ],
            options={
                'verbose_name': 'Share',
                'verbose_name_plural': 'Shares',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lab',
            name='batch_shares',
            field=models.ManyToManyField(to='students.Batch', through='labs.Share'),
            preserve_default=True,
        ),
    ]
