#encoding=utf-8

from django.db import models
from DjangoUeditor.models import UEditorField

class College(models.Model):
    title = models.CharField('培训课程名称', max_length=70)
    position = models.TextField('培训地点', max_length=200, blank=True)
    acttime = models.TextField('培训时间', max_length=200, blank=True)
    excerpt = models.TextField('培训简介', max_length=200, blank=True)
    company = models.TextField('培训单位', max_length=200, blank=True)
    author = models.CharField('培训讲师', max_length=70)
    actfee = models.CharField('培训费用', max_length=70)
    person = models.CharField('人数上限', max_length=70)
    is_help = models.CharField('活动资助', max_length=70)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='培训图片', blank=True, null=True)
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
        verbose_name = '区块链培训'
        verbose_name_plural = '区块链培训'

    def __str__(self):
        return self.title
