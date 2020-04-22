from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index_handler, name='user_index'),
    path('login', views.login_handler, name='user_login'),
    path('register', views.register_handler, name='user_register'),
    path('logout', views.logout_handler, name='user_logout'),
    path('purchasePost', views.purchase_post_handler, name='user_purchase_post'),
    re_path('purchase/(.+)', views.purchase_handler, name='user_purchase'),
    re_path('addShoppingCart/(.+)', views.add_shopping_cart_handler, name='user_addShoppingCart'),
    path('goods', views.goods_handler, name='user_goods'),
    path('shoppingCart', views.shopping_cart, name='user_shoppingCart'),
    re_path('userInfoBuy/(.+)', views.user_info_buy_handler, name='user_info_buy'),
    path('newAddress', views.newAddress_handler, name='user_newAddress'),
    re_path('delAddress/(.+)/(.+)', views.delAddress_handler, name='user_delAddress'),
    re_path('delCode/(.+)', views.delcode_handler, name='user_delcode'),
    path('sumBuy', views.sumbuy_handler, name='user_sumbuy'),
    re_path('delAddress2/(.+)/(.+)', views.delAddress2_handler, name='user_delAddress2'),
    path('newAddress2', views.newAddress2_handler, name='user_newAddress2'),
    path('endPurchase', views.endPurchase_handler, name='user_endPurchase'),
    re_path('delshopcart/(.+)', views.delshopcart_handler, name='user_delshopcart'),
]
