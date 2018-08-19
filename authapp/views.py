from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import MyUserModel


def go_success(request):
    login_name = request.GET.get('login_name', '')
    return render(request, 'auth/success.html', locals())


def go_register(request):
    return render(request, 'auth/register.html')


def reg(request):
    regname = request.POST.get('regname')
    regpwd = request.POST.get('regpwd')
    regtel = request.POST['regtel']
    regqq = request.POST['regqq']
    MyUserModel.objects.create_user(username=regname, password=regpwd, tel=regtel, qq=regqq)  # create_user 会对密码加密
    return HttpResponseRedirect('/authapp/gologin/')


def go_login(request):
    return render(request, 'auth/login.html')


def user_login(request):
    logname = request.POST['logname']
    logpwd = request.POST.get('logpwd')
    user = authenticate(username=logname, password=logpwd)  # 函数认证用户名和密码是否正确
    print('logname', logname, 'logpwd', logpwd, 'user', user)
    if user:
        login(request, user)  # 将用户标识保存到session中
        return HttpResponseRedirect('/authapp/gosuccess/?login_name=' + logname)  # 重定向，并传递get参数
    else:
        return render(request, 'auth/login.html', {'msg': '用户名或密码错误，请重新登陆！'})


@login_required(login_url='/authapp/goreg')
def go_vip(request):
    return render(request, 'auth/user_vip.html')


def log_out(request):
    logout(request)  # logout()函数登出,登出会情况django_session表中所有记录
    return HttpResponseRedirect('/authapp/gologin/')
