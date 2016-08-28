# coding: utf-8

"""
The default configuration is purposefully kept to a minimum.
The Jinja2 backend doesn’t create a Django-flavored environment.
It doesn’t know about Django context processors, filters, and tags.
In order to use Django-specific APIs, you must configure them into the environment.
"""

from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
