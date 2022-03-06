#encoding=utf-8
from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set
import uuid
import pytz
import decimal
import json
from urllib.parse import urlencode
from decimal import Decimal
from datetime import timedelta, datetime, date
from dateutil import parser
import re
import time
import hashlib

from django.utils.timezone import now, localtime
from django.conf import settings
from django.http import JsonResponse, HttpRequest
from django.core.paginator import EmptyPage

from common.paginator import MyPaginator

def ok_json(data) -> JsonResponse:
    return JsonResponse({
        'ok': True,
        'result': data
    })

def error_json(msg:str, code:int=-1, status:int=200) -> JsonResponse:
    return JsonResponse({
        'ok': False,
        'code': code,
        'msg': msg,
    }, status=status)

def utc_now() -> datetime:
    return now()

def current_now() -> datetime:
    return localtime(utc_now())

def str2current_time(select_time, default) -> datetime:
    try:
        return normalize_datetime(parser.parse(select_time))
    except:
        return default

def normalize_datetime(value, tz_name=settings.TIME_ZONE):
    tz = pytz.timezone(tz_name)
    return value.astimezone(tz)

def date_to_str(date_time:date, time_format:str="%Y-%m-%d") -> str:
    return date_time.strftime(time_format)

def utc2str(d:datetime, format_str:str="%Y%m%d%H%M%S") -> str:
    return d.strftime(format_str)

def get_end_of_day(date) -> datetime:
    return datetime(year=date.year,
                    month=date.month,
                    day=date.day,
                    hour=23, minute=59, second=59)

def get_begin_of_day(date) -> datetime:
    return datetime(year=date.year,
                    month=date.month,
                    day=date.day,
                    hour=0, minute=0, second=0)

def generate_uuid() -> str:
    return uuid.uuid4().hex

def vformat(value:Decimal, digits:int=8) -> str:
    fmt = '%%i.%%0%di' % digits
    k = pow(10, digits)

    sign = ''
    if value < 0:
        value = -value
        sign = '-'

    upv = value * k

    r = fmt % (upv // k, upv % k)
    r = sign + r.rstrip('0').rstrip('.')
    if r == '-0':
        r = '0'
    return r

def floor_decimal(amount:Decimal, digits:int=8) -> Decimal:
    return amount.quantize(
        Decimal('1E-%d' % digits),
        context=decimal.Context(rounding=decimal.ROUND_FLOOR))

def parse_int(v:Any, default:int=0) -> int:
    try:
        v = int(v)
    except (ValueError, TypeError) as e:
        v = default
    return v

def parse_decimal(v:Any, default:Any='0', digits:int=8) -> Decimal:
    try:
        return floor_decimal(Decimal(v), digits=digits)
    except decimal.InvalidOperation:
        return Decimal(default)

d0 = Decimal('0')
d1 = Decimal('1')

def parse_date(date_str:str, default="2018-08-08") -> datetime:
    if not date_str:
        date_str = default

    try:
        return parser.parse(date_str)
    except ValueError as e:
        return parser.parse(default)

def get_page(request:HttpRequest) -> int:
    page = parse_int(request.GET.get('page', 1), 1)
    if page < 1:
        page = 1
    return page

PAGE_SIZE = 20
def paged_items(request:HttpRequest, qs, pagesize=PAGE_SIZE, page_cls=MyPaginator):
    paginator = page_cls(qs, pagesize, adjacent_pages=3)
    page = get_page(request)
    try:
        items = paginator.page(page)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    args = {}
    for key, value in request.GET.items():
        if key != "page":
            args[key] = value.encode('utf-8')

    if len(args) == 0:
        items.prefix_uri = request.path + "?"
    else:
        items.prefix_uri = request.path + "?" + urlencode(args) + "&"
    return items

def get_request_ip(request) -> str:
    return request.META.get("HTTP_X_USER_REAL_IP", '') if request else ''

def is_valid_url(url:str) -> bool:
    return not not re.match(r'^https?://[^\s]*', url)

def parse_from_date_and_end_date(request:HttpRequest) -> Tuple[datetime, datetime]:
    query_from_date, query_end_date = request.GET.get('date_range', ' - ').split(' - ')

    from_date = parse_date(query_from_date)
    if not query_end_date:
        query_end_date = date_to_str(utc_now().date())
    end_date = parse_date(query_end_date) + timedelta(hours=23, minutes=59, seconds=59)
    return from_date, end_date

def get_ip_city(ip:str) -> str:
    import geoip2.database
    reader = geoip2.database.Reader('./extra/GeoLite2-City.mmdb')
    res = reader.city(ip)
    return res.city.names.get('zh-CN', '未知')

def sleep(sleep_time:float) -> None:
    time.sleep(sleep_time)

def get_request_info(request, **kwargs):
    if request:
        ip = request.META.get("HTTP_X_USER_REAL_IP", '')
        user_agent = request.META.get("HTTP_USER_AGENT", '')
        cookie = json.dumps(request.COOKIES or {})
    else:
        ip = kwargs.get('ip') or ''
        user_agent = kwargs.get('user_agent') or ''
        cookie = kwargs.get('cookie')
    return ip, user_agent, cookie

def md5(content):
    m = hashlib.md5()
    m.update(content.encode('utf-8'))
    return m.hexdigest()
