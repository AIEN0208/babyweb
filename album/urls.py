from django.urls import path
from django.conf.urls import url, include    # 設定環境變數
from . import views       #從所有app 載入路徑


app_name="album"


urlpatterns = [
    path('',views.index,name='index'),
]