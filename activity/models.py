#encoding=utf-8

from django.db import models
from DjangoUeditor.models import UEditorField

class ActBanner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

class ActivityCat(models.Model):
    name = models.CharField('活动分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='活动排序')

    class Meta:
        verbose_name = '活动分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField('活动地区', max_length=100)
    class Meta:
        verbose_name = '活动地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField('活动标题', max_length=70)
    category = models.ForeignKey(ActivityCat, on_delete=models.DO_NOTHING, verbose_name='活动分类', blank=True, null=True)
    position = models.TextField('活动地点', max_length=200, blank=True)
    tags = models.ManyToManyField(Area, verbose_name='活动地区', blank=True)
    acttime = models.TextField('活动时间', max_length=200, blank=True)
    excerpt = models.TextField('活动摘要', max_length=200, blank=True)
    company = models.TextField('主办单位', max_length=200, blank=True)
    author = models.CharField('活动发起人', max_length=70)
    actfee = models.CharField('活动费用', max_length=70)
    person = models.CharField('人数上限', max_length=70)
    is_help = models.CharField('活动资助', max_length=70)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='活动图片', blank=True, null=True)
    body = UEditorField('内容', width=800, height=500,
                            toolbars="full", imagePath="upimg/", filePath="upfile/",
                            upload_settings={"imageMaxSize": 1204000},
                            settings={}, command=None, blank=True
                        )
    views = models.PositiveIntegerField('阅读量', default=0)
    is_active = models.BooleanField('是否是开启活动', default=True)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = '活动'


    def __str__(self):
        return self.title

