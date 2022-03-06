#encoding=utf-8

from django.contrib import admin
from .models import Newsletter, Advertise


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

