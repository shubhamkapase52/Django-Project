from unicodedata import name
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.first,name='first'),
    path("second", views.second,name='second'),
    path("third", views.third,name='third'),
    path("four", views.four,name='four'),
    path("five", views.five,name='five'),
    path("six", views.six,name='six'),
]
