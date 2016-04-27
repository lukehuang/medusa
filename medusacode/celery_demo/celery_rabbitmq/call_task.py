#!/usr/bin/env python
# coding:utf-8

from celery_tasks import func

result = func.delay()

print type(result)
# <class 'celery.result.AsyncResult'>
print result
# 8ba7ea88-d5db-44b4-8505-82a4c4c0c36f
