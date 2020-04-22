from django.shortcuts import render,HttpResponse
from autoParts.models import *
from django.db.models import Q, F

# Create your views here.


def index_handler(request):
    context = request.context
    logo_category_s = LogoCategory.objects.all()
    part_category_s = PartCategory.objects.all()
    goods_data_logo_s = []
    goods_data_part_s = []
    for logo_category in logo_category_s:
        goods_data_logo_s.append(
            {
                'logo_id': logo_category.id,
                'logo_category': logo_category.name,
                'logo_imgName': logo_category.imgName,
                # 'goods_logo_s': logo_category.pLogoCategory_set.all()
            }
        )
    for part_category in part_category_s:
        goods_data_part_s.append(
            {
                'part_category': part_category.name,
                'goods_part_s': part_category.pPartCategory_set.all()
            }
        )
    context['goods_data_logo_s'] = goods_data_logo_s
    context['goods_data_part_s'] = goods_data_part_s
    return render(request, 'index.html', context)


def goods_handler(request, goods_id):
    context = request.context
    try:
        goods_info = Goods.objects.get(id=goods_id)
        session_user = request.session.get('session_user', None)
        if session_user:
            user_id = session_user['id']
            context['is_buy'] = User.objects.filter(id=user_id, userBuyer_set__id=goods_info.id).exists()
        context['goods_info'] = goods_info
        return render(request, 'goods_info.html', context)
    except Exception as e:
        print(e)
        return HttpResponse('status=404')


def logo_handler(request, logo_id):
    context = request.context
    try:
        logo_goods_s = LogoCategory.objects.get(id=logo_id).pLogoCategory_set.all()
        context['logo_name'] = LogoCategory.objects.get(id=logo_id).name
        context['logo_goods_s'] = logo_goods_s
        return render(request, 'logo_goods.html', context)
    except Exception as e:
        print(e)
        return HttpResponse('status=404')


def search_handler(request):
    context = request.context
    if request.method == 'POST':
        search = request.POST.get('search')
        search_goods_s = Goods.objects.filter(goodsName__icontains=search)
        context['search_goods_s'] = search_goods_s
        return render(request, 'search_goods.html', context)