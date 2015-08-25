# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0003_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.ManyToManyField(to='mdls.Question', null=True, related_name='question_rel_+'),
        ),
    ]
