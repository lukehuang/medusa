# coding: utf-8

"""medusaserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# ----------------------------------------------------------------------------------------------------
# Django admin
"""
Username (leave blank to use 'root'): admin
Password: damin
Email address: admin@163.com
"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
# ----------------------------------------------------------------------------------------------------
# Django REST framework

urlpatterns += (
    url(r'^api/', include('rest.urls')),
)
# ----------------------------------------------------------------------------------------------------
# myapp

urlpatterns += (
    url(r'^', include('myapp.urls')),
)
# ----------------------------------------------------------------------------------------------------
