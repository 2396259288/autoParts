from django.db import models

# Create your models here.


class User(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '用户'
    account = models.CharField(max_length=20, unique=True, verbose_name='账号')
    password = models.CharField(max_length=20, verbose_name='密码')
    username = models.CharField(max_length=25, default='', verbose_name='用户名', blank=True)#blank = True 表单层面可以为空
    money = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='余额')
    gender = models.PositiveSmallIntegerField(default=0, verbose_name='性别', choices=((0,'男'), (1,'女')))#0-男， 1-女
    # choices 设置 元组中的两个值第一个是存在数据库中的值，第二个是显示在用户可视界面中的值
    tel = models.CharField(max_length=11, default='', verbose_name='电话', blank=True)

    def __str__(self):
        return self.account


class Address(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '地址'
    addName = models.CharField(max_length=255, verbose_name='地址')
    addNameUser = models.ForeignKey(to=User, related_name='addNameUser_set', on_delete=models.CASCADE, verbose_name='用户-地址', blank=True)


class BuyRecode(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '购买记录'
    buyAccount = models.CharField(max_length=20, default='', verbose_name='购买用的账号', blank=True)
    buyGoods = models.CharField(max_length=20, default='', verbose_name='购买的物品', blank=True)
    buyAddress = models.CharField(max_length=255, default='', verbose_name='购买用的地址', blank=True)
    buyTel = models.CharField(max_length=11, default='', verbose_name='购买用的电话', blank=True)