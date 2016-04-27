#!/usr/bin/env python
# coding:utf-8

from celery import Celery

"""
BROKER_URL:
transport://user:password@hostname:port/virtual_host
"""
celery_app = Celery(
    main='celery_tasks',
    broker='amqp://celery_user:celery_password@192.168.100.100:5672/celery_vhost',
)

@celery_app.task
def func():
    import datetime
    return datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')

"""
run as celery worker:
celery -A celery_tasks worker --loglevel=info
"""
