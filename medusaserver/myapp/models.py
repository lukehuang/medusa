# coding: utf-8


from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name=u'标题', null=True, max_length=200)
    img = models.CharField(verbose_name=u'图片', null=True, max_length=200)
    link = models.CharField(verbose_name=u'链接', null=True, max_length=200)
    source = models.CharField(verbose_name=u'来源', null=True, max_length=200)
    channel_id = models.CharField(verbose_name=u'频道ID', null=True, max_length=200)
    channel_name = models.CharField(verbose_name=u'频道名称', null=True, max_length=200)
    desc = models.TextField(verbose_name=u'详情', null=True, blank=True)
    datetime_publish = models.DateTimeField(verbose_name=u'发布时间', null=True)
    datetime_created = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
