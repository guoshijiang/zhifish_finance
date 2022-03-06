#encoding=utf-8

from django.contrib import admin
from zhiyu import views
from newsletter import views as newsletter
from activity import views as activity
from college import views as college
from price import views as price
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list-<int:lid>.html', views.list, name='list'),
    path('show-<int:sid>.html', views.show, name='show'),
    path('tag/<tag>', views.tag, name='tags'),
    path('s/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('baidu_verify_mvQbVktnSK.html', views.baidu_verify, name='baidu_verify'),
    path('newsletter/', newsletter.newsletter, name='newsletter'),
    path('price/', price.price, name='price'),
    path('college/', college.college, name='college'),
    path('newsgood/', newsletter.newsgood, name='newsgood'),
    path('newsbad/', newsletter.newsbad, name='newsbad'),
    path('activity/', activity.activity, name='activity'),
    path('activity_show-<int:sid>.html', activity.activity_show, name='activity_show'),
    path('activity_list-<int:lid>.html', activity.activity_list, name='activity_list'),
    path('activity_tag/<tag>', activity.activity_tag, name='activity_tag'),
    path('college/', college.college, name='college'),
    path('college_show-<int:sid>.html', college.college_show, name='college_show'),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
