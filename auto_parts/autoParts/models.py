from django.db import models

import datetime, os
from user.models import User
from time import time
import re

# Create your models here.


def save_img(instance, filename):
    offset_name = filename.rsplit('.', 1)
    filename_new = str(int(time() * 1000))+'.'+offset_name[1]
    return os.path.join('static','img',filename_new)


class LogoCategory(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = 'logo'
    name = models.CharField(max_length=20, unique=True, verbose_name='logo')
    imgName = models.ImageField(upload_to=save_img, verbose_name='logo图片', default='')

    def __str__(self):
        return self.name


class PartCategory(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '部位'
    name = models.CharField(max_length=20, unique=True, verbose_name='部位')

    def __str__(self):
        return self.name


class Goods(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '物品'
    goodsName = models.CharField(max_length=50, verbose_name='物品名称')
    imgName = models.ImageField(upload_to=save_img, verbose_name='物品图片',blank=True)
    pLogoCategory = models.ForeignKey(to=LogoCategory,related_name='pLogoCategory_set', on_delete=models.CASCADE, verbose_name='logo分类',blank=True)
    pPartCategory = models.ForeignKey(to=PartCategory,related_name='pPartCategory_set', on_delete=models.CASCADE, verbose_name='部位分类',blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='价格',blank=True)
    summary = models.CharField(max_length=1000, default='', verbose_name='详细信息',blank=True)
    createDatetime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间',blank=True)
    userBuyer = models.ManyToManyField(to=User, related_name='userBuyer_set', verbose_name='购买用户',blank=True)
    userShoppingcart = models.ManyToManyField(to=User, related_name='userShoppingcart_set', verbose_name='加入购物车用户', blank=True)