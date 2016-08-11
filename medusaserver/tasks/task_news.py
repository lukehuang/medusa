# coding: utf-8

"""
抓取新闻数据
"""

import json

from celery.task import task

import requests


@task()
def get_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return json.loads(response.content)
