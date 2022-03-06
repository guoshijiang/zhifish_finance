#encoding=utf-8

from django.contrib import admin
from .models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fullname', 'logo', 'rank', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'name')