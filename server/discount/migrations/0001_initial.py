# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo_data', '0001_initial'),
        ('money', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('time_start', models.DateField(blank=True, null=True)),
                ('time_end', models.DateField(blank=True, null=True)),
                ('link', models.TextField(blank=True)),
                ('parser', models.CharField(default='UnknownParser', max_length=200)),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_from_city', to='geo_data.City')),
                ('original_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.Currency')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_to_city', to='geo_data.City')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='discount',
            unique_together=set([('from_city', 'to_city')]),
        ),
    ]