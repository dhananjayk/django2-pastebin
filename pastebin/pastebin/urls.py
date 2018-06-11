"""pastebin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from djpaste.views import index, authorize, show_paste
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('authorize/', authorize, name='authorize'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    re_path(r'^(?P<url_key>[0-9A-Za-z]{8,8})', show_paste, name='get_paste'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
