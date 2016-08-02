# coding: utf-8

from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    # 对于无法直接通过HTTP请求下载的资源,添加下载代理通过requests获取资源后修改header来实现浏览器下载
    url(r'^test/download/$', views.DownloadView.as_view(), name='download'),
]
