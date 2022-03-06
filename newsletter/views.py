#encoding=utf-8

import logging
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import F
from django.urls import reverse
from newsletter.models import Newsletter, Advertise
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common.helpers import paged_items, ok_json, error_json, parse_int


def newsletter(request):
    ads = Advertise.objects.all().order_by('-id')[0:6]
    allnewsletter = Newsletter.objects.all().order_by('-id')
    paginator = Paginator(allnewsletter, 20)
    page = request.GET.get('page')
    try:
        allnewsletter = paginator.page(page)
    except PageNotAnInteger:
        allnewsletter = paginator.page(1)
    except EmptyPage:
        allnewsletter = paginator.page(paginator.num_pages)
    if request.is_ajax():
        json_data = serializers.serialize("json", allnewsletter, ensure_ascii=False)
        return ok_json({'newsletter': json_data})
    return render(request, 'newsletter.html', locals())


def newsgood(request):
    news_id = request.GET.get("id")
    Newsletter.objects.filter(id=news_id).update(good=F('good') + 1)
    newsletter_model = Newsletter.objects.filter(id=news_id).values('good')
    total_good = newsletter_model[0]['good']
    return JsonResponse({'total_good': total_good})


def newsbad(request):
    news_id = request.GET.get("id")
    Newsletter.objects.filter(id=news_id).update(bad=F('bad') + 1)
    newsletter_model = Newsletter.objects.filter(id=news_id).values('bad')
    print(newsletter_model)
    total_bad = newsletter_model[0]['bad']
    return JsonResponse({'total_bad': total_bad})
