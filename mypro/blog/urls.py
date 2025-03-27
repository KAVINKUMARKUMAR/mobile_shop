from django.urls import path,include
from . import views

handler404 = 'mypro.views.create_error'

urlpatterns=[
    path("",views.base,name='base'),
    path("index",views.index,name='index'),
]