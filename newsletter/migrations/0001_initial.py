# Generated by Django 2.2.5 on 2019-10-28 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='链接名称')),
                ('linkurl', models.URLField(max_length=100, verbose_name='网址')),
                ('adv_info', models.CharField(default='', max_length=250, verbose_name='广告标题')),
                ('img', models.ImageField(upload_to='advertise/', verbose_name='广告图')),
            ],
            options={
                'verbose_name': '广告',
                'verbose_name_plural': '广告',
            },
        ),
        migrations.CreateModel(
            name='NewsletterCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='快讯分类')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '快讯分类',
                'verbose_name_plural': '快讯分类',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('content', models.TextField(blank=True, default='', verbose_name='快讯内容')),
                ('good', models.PositiveIntegerField(default=0, verbose_name='利好')),
                ('bad', models.PositiveIntegerField(default=0, verbose_name='利空')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='newsletter.NewsletterCat', verbose_name='分类')),
            ],
            options={
                'verbose_name': '快讯',
                'verbose_name_plural': '快讯',
            },
        ),
    ]