from django.urls import path

from homeworkapp import views

app_name = 'homeworkapp'
urlpatterns = [
    path('goregister/', views.register, name='go'),
    path('gostu/', views.querystu, name='stu'),
    path('allstu/',views.showstu,name='stu')
]
