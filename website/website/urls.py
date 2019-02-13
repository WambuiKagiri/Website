"""website URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from accounts.views import (login)
from MySite.views import dashboard


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('MySite.urls')),
    url(r'^', include('django.contrib.auth.urls')), 
    url(r'^accounts/login/',login,name='login'),
    url(r'^agent/',dashboard ,name='dashboard'),
    # url('auth/', include('djoser.urls')),
    # url('auth/', include('djoser.urls.authtoken')),
    # url(r'^', include('chat.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
