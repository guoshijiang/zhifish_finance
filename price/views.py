#encoding=utf-8

import re
import logging
import uuid
import base64
import json
import time
import random
import requests
import sys
import os
import base64

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from django.db import transaction
from django.core.cache import cache
from common.helpers import sleep
from common.helpers import ok_json, error_json
from django.shortcuts import render
from newsletter.models import Advertise

def price(request):
    ads = Advertise.objects.all().order_by('-id')[0:6]
    if request.is_ajax():
    	return ok_json({'data':  api_get()})   	
    return render(request, 'price.html', locals())
    
def api_get(headers=None, timeout=10):
    if headers is None:
        headers = {}
        url = "https://dncapi.bqiapp.com/api/coin/web-coinrank?page=1&type=-1&pagesize=%s&webp=1"
        s_time = time.time()
        resp = requests.get(url, headers=headers, timeout=timeout)
        e_time = time.time()
        if resp.status_code == 502:
            loging.info('respose 502')
        content = resp.content.decode('utf-8')
        try:
            resp_json = json.loads(content)
            if 'ok' not in resp_json or not resp_json['ok']:
                logging.error("bixin: Bot {} send api_get failed: {}".format("zhiyu", content))
            return resp_json
        except ValueError:
            logging.error("bixin: {} return {} {}".format(url, resp.status_code, content))
            raise Exception('{} response status: {} {}'.format(url, resp.status_code, content))
