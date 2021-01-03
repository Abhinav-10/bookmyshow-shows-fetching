# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('row_num', models.PositiveSmallIntegerField()),
                ('col_num', models.PositiveSmallIntegerField()),
                ('status', models.IntegerField(default=1, choices=[(1, b'AVAILABLE'), (2, b'BLOCKED'), (3, b'BOOKED')])),
                ('session', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=30)),
                ('heroine', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('genre', models.CharField(help_text=b'Seperate genre with spaces', max_length=150, null=True)),
                ('language', models.CharField(help_text=b'Seperate language with spaces', max_length=150, null=True)),
                ('description', models.TextField(default=b'Description Text')),
                ('release_date', models.DateField(help_text=b'mm/dd/yyyy')),
                ('runtime_in_minutes', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('trailer', models.CharField(max_length=1000)),
                ('thumbnail_image', models.ImageField(upload_to=b'movie_thumbs')),
                ('slideshow_image', models.ImageField(default=b'true', upload_to=b'movie_thumbs')),
            ],
        ),
        migrations.CreateModel(
            name='screen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('no_of_rows', models.IntegerField(validators=[django.core.validators.MaxValueValidator(75)])),
                ('no_of_columns', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('movie', models.ForeignKey(related_name='show_movie', to='webapp.movie')),
                ('screen', models.ForeignKey(related_name='show_screen', to='webapp.screen')),
            ],
        ),
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('city', models.ForeignKey(related_name='theatre', to='webapp.City')),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='theatre',
            field=models.ForeignKey(related_name='show_theatre', to='webapp.theatre'),
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(related_name='screen', to='webapp.theatre'),
        ),
        migrations.AddField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(related_name='booking_show', to='webapp.show'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(related_name='booking_user', default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('show', 'row_num', 'col_num')]),
        ),
    ]
