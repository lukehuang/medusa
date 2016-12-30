# coding: utf-8

"""
Notice that we're using hyperlinked relations in this case, with [HyperlinkedModelSerializer].
You can also use primary key and various other relationships, but hyperlinking is good RESTful design.
"""

from rest_framework import serializers

from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> News
"""
News
"""
from myapp.models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = (
            'title',
            'img',
            'link',
            'source',
            'channel_id',
            'channel_name',
            'desc',
            'datetime_publish',
            'datetime_created',
            'datetime_updated',
        )
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> News
