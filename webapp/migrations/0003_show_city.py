# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210102_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='city',
            field=models.ManyToManyField(related_name='show_city', to='webapp.City'),
        ),
    ]
