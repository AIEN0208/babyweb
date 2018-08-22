from django.urls import path
from django.conf.urls import url, include    # 設定環境變數
from . import views       #從所有app 載入路徑


app_name="demo"

urlpatterns = [
    path('linebot/', views.linebot, name='linebot'),
    path('eyesnose/', views.eyesnose, name='eyesnose'),
    path('sound/', views.sound, name='sound'),
    path('areas/', views.areas, name='areas'),
    path('emotion/', views.emotion, name='emotion'),
    path('paint/', views.paint, name='paint')
]