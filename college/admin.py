#encoding=utf-8

from django.contrib import admin
from .models import College


@admin.register(College)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'author', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')