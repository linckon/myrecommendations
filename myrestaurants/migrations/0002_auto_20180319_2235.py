# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 22:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myrestaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myrestaurants')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='stateOrProvince',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='street',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='telephone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='zipCode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='myrestaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='restaurantreview',
            unique_together=set([('restaurant', 'user')]),
        ),
    ]
