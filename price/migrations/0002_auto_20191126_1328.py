# Generated by Django 2.2.3 on 2019-11-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='change_percent',
            field=models.CharField(blank=True, max_length=128, verbose_name='change_percent'),
        ),
        migrations.AlterField(
            model_name='price',
            name='coin_code',
            field=models.CharField(blank=True, max_length=128, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='price',
            name='current_price',
            field=models.CharField(blank=True, max_length=128, verbose_name='current_price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='current_price_usd',
            field=models.CharField(blank=True, max_length=128, verbose_name='current_price_usd'),
        ),
        migrations.AlterField(
            model_name='price',
            name='fullname',
            field=models.CharField(blank=True, max_length=128, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='price',
            name='logo',
            field=models.CharField(blank=True, max_length=512, verbose_name='logo'),
        ),
    ]
