from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.index,name='form'),
    url('textchecker/', views.index, name = "Checker"),
    
    # (?# url(r'^textChecker/text=(?P<name>[\w.@+-]+)/$', views.TextChecker, name='TextChecker'),)
]