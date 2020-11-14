from django.urls import path
from . import views

# Hier sind das urls für listings app
# für einzehl die auf liste, nehmen wir das id Nr von diese liste auf path

urlpatterns= [

    path ('', views.index, name='listings'),
    path ('<int:listing_id>', views.listing, name='listing'),
    path ('search', views.search, name='search'),
    
]