# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0005_auto_20150824_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.ManyToManyField(blank=True, related_name='question_rel_+', to='mdls.Question'),
        ),
    ]
