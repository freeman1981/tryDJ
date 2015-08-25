# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0004_auto_20150824_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='mdls.Question', related_name='question_rel_+'),
        ),
    ]
