#!/usr/bin/env python
# coding:utf-8

import logging

rsyslogger = logging.getLogger('rsyslog')


def send_log(tag, msg):
    content = "%s %s" % (tag.replace(' ', ''), msg)
    rsyslogger.info(content)
