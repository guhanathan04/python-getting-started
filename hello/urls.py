from django.conf.urls import include, url
from django.urls import path,re_path
from . import views

urlpatterns = [
    #path('/grammar-checker/',views.index,name='form'),
    #path('grammar-checker/', views.index, name = "Checker"),
    url('^$', views.index, name='index'),
    #path('grammar-checker/<test_string>/', views.index, name='grammar-checker'),
    #url(r'textChecker/text=(?P<text>[\w.@+-]+)/', views.index, name='TextChecker'),
]