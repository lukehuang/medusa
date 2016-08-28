#!/usr/bin/env python
# coding:utf-8

"""
抓取新闻数据
"""

import json
import datetime
import requests
from celery.task import task
from django.db import IntegrityError

from myapp.models import News


URL_NEWS = 'http://apis.baidu.com/showapi_open_bus/channel_news/search_news'
API_KEY = '3a4794e55cf87069b8de63afec1aa09a'


@task()
def get_news():
    response = requests.request(
        method='GET',
        url=URL_NEWS,
        headers={'apikey': API_KEY},
    )
    # data_dict = json.loads(response.content)  # <type 'dict'>
    data_dict = response.json()  # <type 'dict'>

    # print data_dict
    if data_dict['showapi_res_code'] == 0 and data_dict['showapi_res_body']['ret_code'] == 0:
        contentlist = data_dict['showapi_res_body']['pagebean']['contentlist']
        # print contentlist
        news_formatted = [
            {
                'img': content['imageurls'][0]['url'] if content['imageurls'] else None,
                'title': content['title'],
                'datetime_publish': datetime.datetime.strptime(content['pubDate'], '%Y-%m-%d %H:%M:%S'),
                'channel_id': content['channelId'],
                'channel_name': content['channelName'],
                'desc': content['desc'],
                'source': content['source'],
                'link': content['link'],
            } for content in contentlist
        ]
        # print news_formatted

        # [1] 使用 bulk_create 一次性处理多条数据时, 只要数据中有一条与库中重复, 就会导致多条数据无法插入
        # news_list = [
        #     News(
        #         title=content['title'].encode('utf-8'),
        #         img=content['img'],
        #         link=content['link'],
        #         source=content['source'].encode('utf-8'),
        #         channel_id=content['channel_id'],
        #         channel_name=content['channel_name'].encode('utf-8'),
        #         desc=content['desc'].encode('utf-8'),
        #         datetime_publish=content['datetime_publish'],
        #     )
        #     for content in news_formatted
        # ]
        # print news_list
        # News.objects.bulk_create(news_list)

        # [2] 每条数据单独 create 并捕捉 IntegrityError
        for content in news_formatted:
            try:
                News.objects.create(
                    title=content['title'].encode('utf-8'),
                    img=content['img'],
                    link=content['link'],
                    source=content['source'].encode('utf-8'),
                    channel_id=content['channel_id'],
                    channel_name=content['channel_name'].encode('utf-8'),
                    desc=content['desc'].encode('utf-8'),
                    datetime_publish=content['datetime_publish'],
                )
            except IntegrityError, e:
                print e
                pass
