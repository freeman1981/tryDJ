# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0006_auto_20150824_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='from_q',
            field=models.ForeignKey(default=None, related_name='rel_q', to='mdls.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='to_q',
            field=models.ForeignKey(to='mdls.Question', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='rel',
            field=models.ManyToManyField(blank=True, through='mdls.Answer', to='mdls.Question'),
        ),
    ]
