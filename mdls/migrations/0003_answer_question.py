# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0002_auto_20150722_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('entry', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('entry', models.CharField(max_length=100)),
                ('answer', models.ManyToManyField(to='mdls.Answer')),
                ('question', models.ManyToManyField(related_name='question_rel_+', to='mdls.Question')),
            ],
        ),
    ]
