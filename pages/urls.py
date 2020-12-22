from django.urls import path
from . import views

urlpatterns= [
    path ('', views.index, name='index'),
    path ('about', views.about, name='about'),
    path ('restaurant/home', views.home, name='home'),
    path ('restaurant/meal', views.meal, name='meal'),
    path ('restaurant/order', views.order, name='order'),
    path ('restaurant/report', views.home, name='report'),
]