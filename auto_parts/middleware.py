from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
from user.views import login_handler

class MyMiddleware(MiddlewareMixin):
    def __init__(self,get_response=None):
        super().__init__(get_response)
        # 初始化中间件
        print('init_mymiddleware')

    def process_request(self, request):
        print('request.context')
        # 在request对象中添加一个context字典
        request.context = {}
        session_user = None
        # 如果session中有session_user
        if 'session_user' in request.session.keys():
            # 把session中的session_user添加到request.context中
            session_user = request.context['session_user'] = request.session['session_user']
        #未登录的用户不可以直接访问 /user 和 /video 这样的链接
        if not session_user:
            if request.path.startswith('/user') or request.path.startswith('/video'):
                if request.path not in [reverse('user_login'), reverse('user_register')]:
                    return login_handler(request)

    def process_response(self,request,response):
        # 必须return response
        print('process_response')
        return response
