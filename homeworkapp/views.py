from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from homeworkapp.forms import *
from homeworkapp.models import Student


def register(req):
    if req.method == 'POST':
        user = User(req.POST)
        print(user)
        if user.is_valid():
            name = user.cleaned_data['name']
            pwd = user.cleaned_data['password']
            return render(req, 'success.html', locals())
    else:
        sbuser = User()
        return render(req, 'register.html', {'user': sbuser})


@cache_page(30)
def querystu(req):
    students = Student.objects.all()
    return render(req, 'stu.html', locals())


def showstu(req):
    value = cache.get('all')
    if value:
        return render(req, 'stu.html', {'students': value, 'msg': '缓存命中'})
    else:
        students = Student.objects.all()
        cache.set('all',students,30)
        return render(req, 'stu.html', {'students': students, 'msg': '数据库命中'})
