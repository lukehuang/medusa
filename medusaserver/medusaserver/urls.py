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

from rest_framework import routers, serializers, viewsets

from django.contrib.auth.models import User


# Django admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

# ----------------------------------------------------------------------------------------------------
from myapp import views
urlpatterns += (
    # 对于无法直接通过HTTP请求下载的资源,添加下载代理通过requests获取资源后修改header来实现浏览器下载
    url(r'^test/download/$', views.DownloadView.as_view(), name='download'),
)

# ----------------------------------------------------------------------------------------------------
# Django REST framework

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    # add REST framework's login and logout views to use the browsable API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
# ----------------------------------------------------------------------------------------------------
