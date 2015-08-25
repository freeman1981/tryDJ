# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to='foo/media'),
        ),
    ]
