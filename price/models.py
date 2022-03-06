#encoding=utf-8

from django.db import models

class Price(models.Model):
    current_price = models.CharField('current_price', max_length=128, blank=True)
    current_price_usd = models.CharField('current_price_usd', max_length=128, blank=True)
    coin_code = models.CharField('fullname', max_length=128, blank=True)
    name = models.CharField('name', max_length=128)
    fullname = models.CharField('fullname', max_length=128, blank=True)
    logo = models.CharField('logo', max_length=512, blank=True)
    change_percent = models.CharField('change_percent', max_length=128, blank=True)
    market_value = models.CharField('market_value', max_length=128, blank=True)
    vol = models.CharField('vol', max_length=128, blank=True)
    supply = models.CharField('supply', max_length=128)
    rank = models.CharField('rank', max_length=128)
    star_level = models.CharField('star_level', max_length=128)
    kline_data = models.CharField('kline_data', max_length=512)
    market_value_usd =models.CharField('', max_length=128)
    vol_usd = models.CharField('market_value_usd', max_length=128)
    marketcap = models.CharField('marketcap', max_length=128)
    high_price = models.CharField('high_price', max_length=128)
    drop_ath = models.CharField('drop_ath', max_length=128)
    low_price = models.CharField('low_price', max_length=128)
    high_time = models.CharField('high_time', max_length=128) 
    low_time = models.CharField('low_time', max_length=128)
    isifo = models.CharField('isifo', max_length=128)
    ismineable = models.CharField('ismineable', max_length=128)
    advs = models.CharField('advs', max_length=512)
    adpairs = models.CharField('adpairs', max_length=128)
    turnoverrate = models.CharField('turnoverrate', max_length=128)
    changerate_utc = models.CharField('changerate_utc', max_length=128)
    changerate_utc8 = models.CharField('changerate_utc8', max_length=128) 
    created_time = models.DateTimeField('created_time', auto_now_add=True)
    modified_time = models.DateTimeField('', auto_now=True)

    class Meta:
        verbose_name = 'price'
        verbose_name_plural = 'price'

    def __str__(self):
        return self.title
