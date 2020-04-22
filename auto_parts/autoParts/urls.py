from django.contrib import admin
from django.urls import path, re_path
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_handler, name='autoparts_index'),
    re_path('goods/(.+)', views.goods_handler, name='autoparts_goods'),
    re_path('logo/(.+)', views.logo_handler, name='autoparts_logo'),
    path('search/', views.search_handler, name='autoparts_search'),
]
