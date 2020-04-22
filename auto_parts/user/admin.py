from django.contrib import admin
from user.models import User, Address, BuyRecode

# Register your models here.
admin.site.site_header = '后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 设置类对象的anmin中的显示
    # 设置显示样式
    list_display = ['id', 'account', 'username', 'gender', 'money', 'tel']
    # 设置过滤器
    list_filter = ['gender']
    # 设置搜索 列表中表示可以根据什么搜索
    search_fields = ['account', 'username']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    # 设置类对象的anmin中的显示
    # 设置显示样式
    list_display = ['addName', 'addNameUser']
    # 设置过滤器
    list_filter = ['addNameUser']


@admin.register(BuyRecode)
class AddressAdmin(admin.ModelAdmin):
    # 设置类对象的anmin中的显示
    # 设置显示样式
    list_display = ['buyAccount', 'buyGoods', 'buyAddress', 'buyTel']
    # 设置过滤器
    list_filter = ['buyAccount']