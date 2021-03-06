"""babyweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'album', views.AlbumViewSet)
router.register(r'paint', views.PaintViewSet)
router.register(r'covered', views.CoveredViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    url(r'login/$',views.login, name = 'login'),
    path('member/', include('member.urls')),
    path('album/', include('album.urls')),
    url(r'^api/', include(router.urls)),
    path('demo/', include('demo.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
