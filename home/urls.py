from django.urls import path,include    # 設定環境變數
from . import views       #從所有app 載入路徑

app_name="home"
urlpatterns = [
    path('',views.index,name='index'),
]