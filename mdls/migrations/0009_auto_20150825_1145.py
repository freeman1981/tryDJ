# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0008_auto_20150825_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='to_q',
            field=models.ForeignKey(to='mdls.Question'),
        ),
    ]
