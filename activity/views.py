#encoding=utf-8

import time, datetime
from django.core import serializers
from django.shortcuts import render
from activity.models import Activity, ActBanner, Area, ActivityCat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import reverse,redirect
from common.helpers import paged_items, ok_json, error_json, parse_int


def activity(request):
    act_banner = ActBanner.objects.filter(is_active=True)[0:6]
    actcat = ActivityCat.objects.all()
    area = Area.objects.all()
    hot_act = Activity.objects.filter(is_active=True).order_by('views')[:8]
    allarticle = Activity.objects.all().order_by('-id')
    paginator = Paginator(allarticle, 18)
    page = request.GET.get('page')
    try:
        allarticle = paginator.page(page)
    except PageNotAnInteger:
        allarticle = paginator.page(1)
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)
    if request.is_ajax():
        json_data = serializers.serialize("json", allarticle, ensure_ascii=False)
        return ok_json({'activity': json_data})
    return render(request, 'activity.html', locals())


def activity_show(request,sid):
    activity_show = Activity.objects.get(id=sid)
    hot_activity = Activity.objects.all().order_by('?')[:10]
    previous_blog = Activity.objects.filter(created_time__gt=activity_show.created_time,category=activity_show.category.id).first()
    netx_blog = Activity.objects.filter(created_time__lt=activity_show.created_time,category=activity_show.category.id).last()
    activity_show.views = activity_show.views + 1
    activity_show.save()
    return render(request, 'activity_show.html', locals())


def activity_tag(request, tag):
    act_list = Activity.objects.filter(tags__name=tag)
    tname = Area.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(act_list, 18)
    try:
        act_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        act_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        act_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'activity_tag.html', locals())


def activity_list(request,lid):
    act_list = Activity.objects.filter(category_id=lid)
    cname = ActivityCat.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(act_list, 18)
    try:
        act_list = paginator.page(page)
    except PageNotAnInteger:
        act_list = paginator.page(1)
    except EmptyPage:
        act_list = paginator.page(paginator.num_pages)
    return render(request, 'activity_list.html', locals())



