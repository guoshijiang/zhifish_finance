#encoding=utf-8

import time, datetime
from django.core import serializers
from django.shortcuts import render
from college.models import College
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import reverse,redirect
from common.helpers import paged_items, ok_json, error_json, parse_int

def college(request):
    allcollege= College.objects.all().order_by('-id')
    paginator = Paginator(allcollege, 18)
    page = request.GET.get('page')
    try:
        allcollege = paginator.page(page)
    except PageNotAnInteger:
        allcollege = paginator.page(1)
    except EmptyPage:
        allcollege = paginator.page(paginator.num_pages)
    return render(request, 'college.html', locals())


def college_show(request,sid):
    collegeshow = College.objects.get(id=sid)
    previous_blog = College.objects.filter(created_time__gt=collegeshow.created_time).first()
    netx_blog = College.objects.filter(created_time__lt=collegeshow.created_time).last()
    collegeshow.views = collegeshow.views + 1
    collegeshow.save()
    return render(request, 'college_show.html', locals())

