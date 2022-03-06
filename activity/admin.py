#encoding=utf-8

from django.contrib import admin
from .models import ActivityCat, Area, Activity, ActBanner


@admin.register(Activity)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'company', 'author', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')


@admin.register(ActBanner)
class ActBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(ActivityCat)
class ActivityCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

