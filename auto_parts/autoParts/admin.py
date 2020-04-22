from django.contrib import admin
from autoParts.models import Goods, LogoCategory, PartCategory

# Register your models here.


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    filter_horizontal = ['userBuyer', 'userShoppingcart']
    list_display = ['id', 'goodsName', 'pLogoCategory', 'pPartCategory', 'price', 'summary', 'createDatetime']
    list_filter = ['createDatetime']


@admin.register(LogoCategory)
class LogoCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PartCategory)
class PartCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
