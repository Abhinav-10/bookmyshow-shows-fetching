# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='city',
        ),
        migrations.AddField(
            model_name='theatre',
            name='city',
            field=models.ManyToManyField(related_name='theatre', to='webapp.City'),
        ),
    ]
