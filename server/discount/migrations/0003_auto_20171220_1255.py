# Generated by Django 2.0 on 2017-12-20 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_auto_20171118_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='original_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='money.Currency'),
        ),
    ]