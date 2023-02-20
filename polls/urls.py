from django.contrib import admin
from django.urls import path
from .views import hellofunc  # hellofuncの場所(.views)

urlpatterns = [
    path("hello/", hellofunc),  # 'hello/'のリクエストを受け取ったら、hellofuncを操作
]
