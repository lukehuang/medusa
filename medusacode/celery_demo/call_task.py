#!/usr/bin/env python
# coding:utf-8

"""
call celery tasks
"""

import random

from celery_tasks import func

n = random.randint(1, 5)
result = func.delay(n)

print type(result)
# <class 'celery.result.AsyncResult'>

print result
# 8ba7ea88-d5db-44b4-8505-82a4c4c0c36f

# Wait until task is ready, and return its result.
print result.get()
