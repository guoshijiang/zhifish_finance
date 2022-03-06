# Generated by Django 2.2.3 on 2019-11-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.TextField(blank=True, max_length=128, verbose_name='current_price')),
                ('current_price_usd', models.TextField(blank=True, max_length=128, verbose_name='current_price_usd')),
                ('coin_code', models.TextField(blank=True, max_length=128, verbose_name='fullname')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('fullname', models.TextField(blank=True, max_length=128, verbose_name='fullname')),
                ('logo', models.TextField(blank=True, max_length=512, verbose_name='logo')),
                ('change_percent', models.TextField(blank=True, max_length=128, verbose_name='change_percent')),
                ('market_value', models.TextField(blank=True, max_length=128, verbose_name='market_value')),
                ('vol', models.TextField(blank=True, max_length=128, verbose_name='vol')),
                ('supply', models.CharField(max_length=128, verbose_name='supply')),
                ('rank', models.CharField(max_length=128, verbose_name='rank')),
                ('star_level', models.CharField(max_length=128, verbose_name='star_level')),
                ('kline_data', models.CharField(max_length=512, verbose_name='kline_data')),
                ('market_value_usd', models.CharField(max_length=128, verbose_name='')),
                ('vol_usd', models.CharField(max_length=128, verbose_name='market_value_usd')),
                ('marketcap', models.CharField(max_length=128, verbose_name='marketcap')),
                ('high_price', models.CharField(max_length=128, verbose_name='high_price')),
                ('drop_ath', models.CharField(max_length=128, verbose_name='drop_ath')),
                ('low_price', models.CharField(max_length=128, verbose_name='low_price')),
                ('high_time', models.CharField(max_length=128, verbose_name='high_time')),
                ('low_time', models.CharField(max_length=128, verbose_name='low_time')),
                ('isifo', models.CharField(max_length=128, verbose_name='isifo')),
                ('ismineable', models.CharField(max_length=128, verbose_name='ismineable')),
                ('advs', models.CharField(max_length=512, verbose_name='advs')),
                ('adpairs', models.CharField(max_length=128, verbose_name='adpairs')),
                ('turnoverrate', models.CharField(max_length=128, verbose_name='turnoverrate')),
                ('changerate_utc', models.CharField(max_length=128, verbose_name='changerate_utc')),
                ('changerate_utc8', models.CharField(max_length=128, verbose_name='changerate_utc8')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'price',
            },
        ),
    ]