from django.urls import path

from authapp.views import *

app_name = 'authapp'

urlpatterns = [
    path('goreg/', go_register),
    path('reg/', reg, name='reg'),
    path('gologin/', go_login, name='gologin'),
    path('login/', user_login, name='login'),
    path('gosuccess/', go_success),
    path('go_vip/', go_vip),
    path('logout/', log_out, name='logout'),
]
