# coding: utf-8

from django.conf.urls import url, include
from rest_framework import routers
from rest import views

"""
Because we're using viewsets instead of views,
we can automatically generate the URL conf for our API,
by simply registering the viewsets with a router class.
"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

"""
Again, if we need more control over the API URLs,
we can simply drop down to using regular class-based views, and writing the URL conf explicitly.
"""

"""
Finally, we're including default login and logout views for use with the browsable API.
That's optional, but useful if your API requires authentication and you want to use the browsable API.
"""

urlpatterns = [
    # Wire up our API using automatic URL routing.
    url(r'^', include(router.urls)),
    # Additionally, we include login URLs for the browsable API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
