# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batchs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference', models.IntegerField(default=0)),
                ('lab', models.ForeignKey(to='labs.Lab')),
            ],
            options={
                'verbose_name': 'Lab Group',
                'verbose_name_plural': 'Lab Groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phase', models.CharField(max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('is_selected', models.BooleanField(default=False)),
                ('selection_score', models.IntegerField(default=0)),
                ('lab', models.ForeignKey(to='labs.Lab')),
            ],
            options={
                'verbose_name': 'Selection',
                'verbose_name_plural': 'Selections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('batch', models.ForeignKey(to='students.Batch')),
                ('group_preferences', models.ManyToManyField(to='labs.Lab', null=True, through='students.GroupPreference', blank=True)),
                ('lab', models.ForeignKey(related_name='assigned_set', blank=True, to='labs.Lab', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Group',
                'verbose_name_plural': 'Student Groups',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='studentgroup',
            field=models.ForeignKey(to='students.StudentGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='selection',
            name='student_group',
            field=models.ForeignKey(to='students.StudentGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grouppreference',
            name='student_group',
            field=models.ForeignKey(to='students.StudentGroup'),
            preserve_default=True,
        ),
    ]
