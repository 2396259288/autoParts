from django.shortcuts import render,HttpResponse,redirect,reverse
from user.models import *
from autoParts.models import *
from autoParts import views as ap_views
# Create your views here.


def index_handler(request):
    context = request.context
    session_user = request.session['session_user']
    user_id = session_user['id']
    user = User.objects.get(id=user_id)
    context['user'] = user
    if request.method == 'GET':
        return render(request, 'user_index.html', context)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.gender = request.POST.get('gender')
        user.tel = request.POST.get('tel')
        user.save()
        return redirect(reverse('user_index'))


def login_handler(request):
    context = request.context
    if request.method != 'POST':
        return render(request, 'login.html')
    account = request.POST.get('account')
    password = request.POST.get('password')
    user_s = User.objects.filter(account=account, password=password)
    if user_s:
        user = user_s[0]
        request.session['session_user'] = {'id': user.id, 'account': user.account}
        # return redirect(reverse('course_index'))
        context['session_user'] = request.session['session_user']
        '''
        因为return course_views.index(request)不会过中间件，所以在这里做重定向，
        或重新给context添加session_user
        '''
    else:
        context['login_message'] = '账号密码错误'
        return render(request, 'login.html', context)
    return ap_views.index_handler(request)


def register_handler(request):
    context = request.context
    if request.method != 'POST':
        return render(request, 'register.html')
    account = request.POST.get('account')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    # email = request.POST.get('email')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    try:
        user_exists = User.objects.filter(account=account).exists()
        if not user_exists:
            if password == confirm_password:
                user = User(account=account,
                            password=password,
                            tel=tel,
                            gender=gender)
                user.save()
                request.session['session_user'] = {'id': user.id, 'account': user.account}
            else:
                context['register_message'] = '两次密码不相同'
                return render(request, 'register.html', context)
        else:
            context['register_message'] = '账号已存在'
            return render(request, 'register.html', context)
    except Exception as e:
        print(e)
        context['register_message'] = '服务器异常'
        return render(request, 'register.html', context)

    return render(request, 'tiaozhuan.html')


def logout_handler(request):
    context = request.context
    request.session['session_user'] = None
    context['session_user'] = request.session['session_user']
    return ap_views.index_handler(request)


def purchase_handler(request, goods_id):
    context = request.context
    try:
        goods = Goods.objects.get(id=goods_id)
        session_user = request.session['session_user']
        user = User.objects.get(id=session_user.get('id'))
        if user.money >= goods.price:
            user.userBuyer_set.add(goods)
            user.money = user.money - goods.price
            user.save()
            context['message'] = '购买成功'
        else:
            context['message'] = '余额不足'
    except Exception as e:
        print(e)
        context['message'] = '购买失败'
    finally:
        return render(request, 'user_message.html', context)


def add_shopping_cart_handler(request, goods_id):
    context = request.context
    try:
        goods = Goods.objects.get(id=goods_id)
        session_user = request.session['session_user']
        user = User.objects.get(id=session_user.get('id'))
        user.userShoppingcart_set.add(goods)
        user.save()
        context['message'] = '添加购物车成功'
    except Exception as e:
        print(e)
        context['message'] = '添加购物车失败'
    return render(request, 'user_message.html', context)


# def goods_handler(request):
#     context = request.context
#     session_user = request.session['session_user']
#     print(session_user.get('account'))
#     goods_s = User.objects.get(id=session_user.get('id')).userBuyer_set.all()
#     context['goods_s'] = goods_s
#     return render(request, 'user_goods.html', context)

def goods_handler(request):
    context = request.context
    session_user = request.session['session_user']
    goods_s = BuyRecode.objects.filter(buyAccount=session_user.get('account')).all()
    context['goods_s'] = goods_s
    return render(request, 'user_goods.html', context)


def shopping_cart(request):
    context = request.context
    session_user = request.session['session_user']
    goods_s = User.objects.get(id=session_user.get('id')).userShoppingcart_set.all()
    context['goods_s'] = goods_s
    return render(request, 'user_shoppingcart.html', context)


def user_info_buy_handler(request, goods_id):
    context = request.context
    session_user = request.session['session_user']
    address_s = User.objects.get(id=session_user.get('id')).addNameUser_set.all()
    context['address_s'] = address_s
    context['goods_id'] = goods_id
    return render(request, 'user_info_buy.html', context)


def purchase_post_handler(request):
    if request.method == 'POST':
        goods_id = request.POST.get('goodsID')
        address = request.POST.get('address')
        payment = request.POST.get('payment')
        context = request.context
        try:
            goods = Goods.objects.get(id=goods_id)
            session_user = request.session['session_user']
            user_id = session_user.get('id')
            goods.userShoppingcart.remove(user_id)
            user = User.objects.get(id=user_id)
            if payment == '1':
                if user.money >= goods.price:
                    user.userBuyer_set.add(goods)
                    user.money = user.money - goods.price
                    user.save()
                    context['message'] = '购买成功'
                    buy_recode = BuyRecode(
                        buyAccount=user.account,
                        buyAddress=address,
                        buyGoods=goods.goodsName,
                        buyTel=user.tel,
                    )
                    buy_recode.save()
                else:
                    context['message'] = '余额不足'
            else:
                buy_recode = BuyRecode(
                    buyAccount=user.account,
                    buyAddress=address,
                    buyGoods=goods.goodsName,
                    buyTel=user.tel,
                )
                buy_recode.save()
                context['message'] = '购买成功'
        except Exception as e:
            print(e)
            context['message'] = '购买失败'
        finally:
            return render(request, 'user_message.html', context)
    else:
        return HttpResponse('method, false, get')


def newAddress_handler(request):
    if request.method == 'POST':
        goods_id = request.POST.get('goodsID')
        session_user = request.session['session_user']
        address = Address(
            addName=request.POST.get('newAddress'),
            addNameUser_id=session_user.get('id')
        )
        address.save()
        # return user_info_buy_handler(request, goods_id=goods_id)
        return redirect(reverse('user_info_buy', args=goods_id))


def delAddress_handler(request, address_id, goods_id):
    address_id = address_id
    goods_id = goods_id
    Address.objects.get(id=address_id).delete()
    return redirect(reverse('user_info_buy', args=goods_id))


def delcode_handler(request, goods_id):
    BuyRecode.objects.get(id=goods_id).delete()
    return redirect(reverse('user_goods'))


def sumbuy_handler(request):
    context = request.context
    session_user = request.session['session_user']
    address_s = User.objects.get(id=session_user.get('id')).addNameUser_set.all()
    context['address_s'] = address_s
    request.session['sumpay'] = 0
    if request.session['sumpay'] != 0:
        sumpay = request.session['sumpay']
        context['sumpay'] = sumpay
    if request.method == "POST":
        buy_goods = request.POST.getlist('buyGoods')
        buy_numbers = request.POST.getlist('goods_num')
        # context['buy_goods'] = buy_goods
        # context['buy_numbers'] = buy_numbers
        sumpay = 0
        for i in range(len(buy_goods)):
            sumpay = sumpay + int(buy_numbers[i]) * int(Goods.objects.get(id=buy_goods[i]).price)
        context['sumpay'] = sumpay
        request.session['sumpay'] = sumpay
        request.session['buy_goods'] = buy_goods
    return render(request, 'sum_purchase.html', context)


def delAddress2_handler(request, address_id, sumpay):
    request.session['sumpay'] = sumpay
    address_id = address_id
    Address.objects.get(id=address_id).delete()
    return redirect(reverse('user_sumbuy'))


def newAddress2_handler(request):
    if request.method == 'POST':
        request.session['sumpay'] = request.POST.get('sumpay')
        session_user = request.session['session_user']
        address = Address(
            addName=request.POST.get('newAddress'),
            addNameUser_id=session_user.get('id')
        )
        address.save()
    return redirect(reverse('user_sumbuy'))


def endPurchase_handler(request):
    context = request.context
    session_user = request.session['session_user']
    user_id = session_user.get('id')
    if request.method == "POST":
        address = request.POST.get('address')
        buy_goods = request.session['buy_goods']
        try:
            for buy_item in buy_goods:
                goods = Goods.objects.get(id=buy_item)
                goods.userShoppingcart.remove(user_id)
                session_user = request.session['session_user']
                user = User.objects.get(id=session_user.get('id'))
                buy_recode = BuyRecode(
                    buyAccount=user.account,
                    buyAddress=address,
                    buyGoods=goods.goodsName,
                    buyTel=user.tel,
                )
                buy_recode.save()
            context['message'] = '购买成功'
        except Exception as e:
            print(e)
            context['message'] = '购买失败'
        finally:
            return render(request, 'user_message.html', context)


def delshopcart_handler(request, goods_id):
    session_user = request.session['session_user']
    goods = Goods.objects.get(id=goods_id)
    user_id = session_user.get('id')
    goods.userShoppingcart.remove(user_id)
    return redirect(reverse('user_shoppingCart'))