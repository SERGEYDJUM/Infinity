from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('about', views.about, name='about'),
    path('chat', views.chat, name='chat'),
    path('lib', views.lib, name='lib'),
    path('account', views.account, name='account'),
    path('logout', views.logout, name='logout'),
]
