from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('lib', views.lib, name='lib'),
    path('account', views.account, name='account')
]
