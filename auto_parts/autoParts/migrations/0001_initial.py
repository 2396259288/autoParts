# Generated by Django 2.2 on 2020-02-18 14:41

import autoParts.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='logo')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='部位')),
            ],
            options={
                'verbose_name': '部位',
                'verbose_name_plural': '部位',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsName', models.CharField(max_length=50, verbose_name='物品名称')),
                ('imgName', models.ImageField(upload_to=autoParts.models.save_img, verbose_name='物品图片')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, verbose_name='价格')),
                ('summary', models.CharField(blank=True, default='', max_length=1000, verbose_name='详细信息')),
                ('createDatetime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 18, 22, 41, 28, 625439), verbose_name='创建时间')),
                ('pLogoCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pLogoCategory_set', to='autoParts.LogoCategory', verbose_name='logo分类')),
                ('pPartCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pPartCategory_set', to='autoParts.PartCategory', verbose_name='部位分类')),
                ('userBuyer', models.ManyToManyField(blank=True, related_name='userBuyer_set', to='user.User', verbose_name='购买用户')),
                ('userShoppingcart', models.ManyToManyField(blank=True, related_name='userShoppingcart_set', to='user.User', verbose_name='加入购物车用户')),
            ],
            options={
                'verbose_name': '物品',
                'verbose_name_plural': '物品',
            },
        ),
    ]