from django.urls import path
from django.conf.urls import url, include    # 設定環境變數
from . import views       #從所有app 載入路徑


app_name="album"


urlpatterns = [
    path('',views.index,name='index'),
    path('paint/', views.paint, name='paint'),
    path('covered/', views.covered, name='covered'),
    path('dalbum/<int:id>/', views.dalbum,name='dalbum'),
    path('dpaint/<int:id>/', views.dpaint,name='dpaint'),
    path('dcovered/<int:id>/', views.dcovered,name='dcovered'),
]