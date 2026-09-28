from django.urls import path
from . import views

# 網頁路徑 網頁在 views 裡的功能 名稱
urlpatterns = [
    path('', views.home, name = "home"),
]
