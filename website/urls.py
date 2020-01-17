#Website urls

from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='index'),
    path('contact',views.Contact, name='contact'),
    path('galery',views.Gallery, name='gallery'),
    path('onama',views.Onama, name='onama'),
    
]