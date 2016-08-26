#!/usr/bin/env python
# coding:utf-8

import datetime

import requests

URL_NEWS = 'http://apis.baidu.com/showapi_open_bus/channel_news/search_news'
API_KEY = '3a4794e55cf87069b8de63afec1aa09a'

response = requests.request(
    method='GET',
    url=URL_NEWS,
    headers={'apikey': API_KEY},
)

data_dict = response.json()  # <type 'dict'>
# print data_dict

if data_dict['showapi_res_code'] == 0 and data_dict['showapi_res_body']['ret_code'] == 0:
    contentlist = data_dict['showapi_res_body']['pagebean']['contentlist']
    print contentlist

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

    print news_formatted
