#encoding=utf-8

from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    title = models.CharField('标题', max_length=70)
    content = models.TextField('快讯内容', default='', blank=True)
    good = models.PositiveIntegerField('利好', default=0)
    bad = models.PositiveIntegerField('利空', default=0)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '快讯'
        verbose_name_plural = '快讯'

    def __str__(self):
        return self.title


class Advertise(models.Model):
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)
    adv_info = models.CharField('广告标题', max_length=250, default='')
    img = models.ImageField('广告图', upload_to='advertise/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = '广告'
