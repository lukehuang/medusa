#!/usr/bin/env python
# coding:utf-8

import os
import time
import datetime
import random
import json
import multiprocessing
import threading
import logging

from django.conf import settings
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile, TemporaryUploadedFile
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from myapp.models import News

import requests


class DownloadView(View):
    """
    文件下载功能测试
    """
    # # [1] 文件流(string)
    # def get(self, request, *args, **kwargs):
    #     # os.getcwd() = '/home/workspace/medusa/medusaserver'
    #     file_download = 'README.md'
    #     with open(file_download) as f:
    #         content = f.read()
    #     response = HttpResponse(content)
    #     response['Content-Type'] = 'application/octet-stream'
    #     response['Content-Disposition'] = 'attachment;filename="%s"' % file_download
    #     return response

    # # [2] 迭代器(iterator)
    # def get(self, request, *args, **kwargs):
    #     # an iterator that yields strings as content
    #     def file_iterator(file_name, size_byte=64):
    #         with open(file_name) as f:
    #             while True:
    #                 content = f.read(size_byte)
    #                 if content:
    #                     yield content
    #                 else:
    #                     break
    #     # os.getcwd() = '/home/workspace/medusa/medusaserver'
    #     file_download = 'README.md'
    #     response = HttpResponse(file_iterator(file_download))
    #     response['Content-Type'] = 'application/octet-stream'
    #     response['Content-Disposition'] = 'attachment;filename="%s"' % file_download
    #     return response

    # [3] 下载代理(利用requests实现)
    def get(self, request, *args, **kwargs):
        # url = 'http://records.cloud.chivox.com/57a004e72bedada5b80109f3.mp3'
        # url = 'http://photos.breadtrip.com/photo_2016_06_25_b696dd78fbb4be3c42a2bb421296bc9e.jpg'
        url = request.GET.get('url')
        basename = os.path.basename(url)
        resp = requests.get(url)
        response = HttpResponse(content=resp.content)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="%s"' % basename
        return response


class TestTemplateView(View):
    """
    渲染模板
    """
    def get(self, request, *args, **kwargs):
        context = {}
        context.update(none_value=None)
        template = 'test.html'
        return render_to_response(template, context)


class TreeView(View):
    """
    echarts 显示树状结构
    """
    def get(self, request, *args, **kwargs):
        context = {}
        a, b, c, d, e, f, g = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
        tree = {
            a: [b, c],
            b: [d, e],
            c: [],
            d: [f, g],
            e: [],
            f: [],
            g: [],
        }
        context.update(tree=tree)
        template = 'tree.html'
        return render_to_response(template, context)




class NewsListView(View):
    """
    新闻列表
    """
    def get(self, request, *args, **kwargs):
        print '================================================================================'
        process = multiprocessing.current_process()
        thread = threading.current_thread()
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        process_thread_info = '(datetime=%s) [Process: %s %s %s] [Thread: %s %s %s]' % \
                              (
                                  dt,
                                  process.name, process.pid, id(process),
                                  thread.getName(), thread.ident, id(thread),
                              )
        print process_thread_info
        print '================================================================================'
        # 关键字参数和分页参数
        keyword = request.GET.get('keyword')
        page = request.GET.get('page', 1)
        # 查询数据库
        news = News.objects.order_by('-datetime_updated')
        # 过滤掉没有图片的新闻条目
        news = news.filter(img__isnull=False)
        if keyword:
            strict = Q(title__icontains=keyword) | \
                     Q(desc__icontains=keyword)
            news = news.filter(strict)
            pass
        # 分页
        paginator = Paginator(object_list=news, per_page=10)
        try:
            pager = paginator.page(page)
        except PageNotAnInteger:
            pager = paginator.page(1)
        except EmptyPage:
            pager = paginator.page(paginator.num_pages)
            pass
        # 分页片段中使用 pager.queries 达到在翻页时带着查询参数的目的
        pager.queries = "keyword=%s" % (keyword or '',)
        # [网页模板]和[通用分页片段(pagination_jinja.html)]中使用 "page" 来访问 Page object
        context = dict()
        context['keyword'] = keyword
        context['page'] = pager
        return render_to_response('news_list.html', context)


class SentryTestView(View):
    """
    测试 Sentry ( Raven captureException & captureMessage )
    """
    def get(self, request, *args, **kwargs):
        try:
            1/0
        except Exception, e:
            from raven.contrib.django.raven_compat.models import client
            # Capture an Error
            client.captureException()
            # Reporting an Event
            client.captureMessage('This is a message sent from medusaserver by client.captureMessage()')
        return HttpResponse()


class ExceptionTestView(View):
    """
    INSTALLED_APPS = (
        'raven.contrib.django.raven_compat',
    )
    This causes Raven to install a hook in Django that will automatically report uncaught exceptions.
    """
    def get(self, request, *args, **kwargs):
        ret = 1/0
        return HttpResponse(ret)


class SentryLogTestView(View):
    """
    测试 Sentry ( Sentry Log )
    """
    def get(self, request, *args, **kwargs):
        try:
            1/0
        except Exception, e:
            """
            Logging usage works the same way as it does outside of Django,
            with the addition of an optional request key in the extra data:
            """
            import logging
            logger = logging.getLogger('sentry')
            logger.error(
                msg='ERROR: %s' % str("This is from logging.getLogger('sentry').error(): %s" % str(e)),
                exc_info=True,
                extra={
                'request': request,  # Optionally pass a request and we'll grab any information we can
                }
            )
        return HttpResponse()




class ProcessThreadView(View):
    """
    Django threads:
    [1] runserver (the development server) starts a new thread for every request;
    [2] gunicorn reuses threads across requests;
    """
    def get(self, request, *args, **kwargs):
        print '================================================================================'
        process = multiprocessing.current_process()
        thread = threading.current_thread()
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        process_thread_info = '(datetime=%s) [Process: %s %s %s] [Thread: %s %s %s]' % \
                              (
                                  dt,
                                  process.name, process.pid, id(process),
                                  thread.getName(), thread.ident, id(thread),
                              )
        print process_thread_info
        print '================================================================================'
        return HttpResponse(process_thread_info)




class RsyslogView(View):
    """
    测试 rsyslog
    """
    def get(self, request, *args, **kwargs):
        rsyslogger = logging.getLogger('rsyslog')
        print '>>>>>>>>>> rsyslogger: ', rsyslogger

        msg = 'tag1 This is a rsyslog : %s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        rsyslogger.info(msg)

        msg = 'tag2 This is a rsyslog : %s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        rsyslogger.info(msg)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        from lib.rsyslog.rsyslog_utils import send_log
        send_log('tag3', 'This is a message with tag: tag3, datetime is %s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        return HttpResponse(msg)




class TimeoutView(View):
    """
    测试 Timeout
    """
    def get(self, request, *args, **kwargs):
        sleep_time = 5
        time.sleep(sleep_time)
        return HttpResponse('Sleep Time = %s' % sleep_time)




class MakoView(View):
    """
    测试 Mako Template
    """
    def get(self, request, *args, **kwargs):
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # [1] Template
        # from mako.template import Template
        # template = Template(
        #     filename='/home/workspace/medusa/medusaserver/myapp/templates/mako.html',
        #     input_encoding='utf-8',
        #     output_encoding='utf-8',
        # )
        # context = {'key': 'value'}
        # html = template.render(data=context)
        # print html
        # return HttpResponse(html)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # [2] TemplateLookup
        from mako.lookup import TemplateLookup
        template_path = '/home/workspace/medusa/medusaserver/myapp/templates'
        lookup = TemplateLookup(
            directories=[template_path],
            module_directory='/home/workspace/medusa/medusaserver/myapp/templates/mako_modules',
            input_encoding='utf-8',
            output_encoding='utf-8',
        )
        template = lookup.get_template('mako.html')
        context = {'key': 'value'}
        html = template.render(data=context)
        print html
        return HttpResponse(html)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




class NewsMakoView(View):
    """
    新闻列表(Mako Template)
    """
    def get(self, request, *args, **kwargs):
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # 关键字参数和分页参数
        keyword = request.GET.get('keyword')
        page = request.GET.get('page', 1)
        # 查询数据库
        news = News.objects.order_by('-datetime_updated')
        # 过滤掉没有图片的新闻条目
        news = news.filter(img__isnull=False)
        if keyword:
            strict = Q(title__icontains=keyword) | \
                     Q(desc__icontains=keyword)
            news = news.filter(strict)
            pass
        # 分页
        paginator = Paginator(object_list=news, per_page=10)
        try:
            pager = paginator.page(page)
        except PageNotAnInteger:
            pager = paginator.page(1)
        except EmptyPage:
            pager = paginator.page(paginator.num_pages)
            pass
        # 分页片段中使用 pager.queries 达到在翻页时带着查询参数的目的
        pager.queries = "keyword=%s" % (keyword or '',)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        from mako.template import Template
        from mako.lookup import TemplateLookup
        template_path = '/home/workspace/medusa/medusaserver/myapp/templates'
        lookup = TemplateLookup(
            directories=[template_path],
            module_directory='/home/workspace/medusa/medusaserver/myapp/templates/mako_modules',
            input_encoding='utf-8',
            output_encoding='utf-8',
        )
        template = lookup.get_template('news_list_mako.html')
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # [网页模板]和[通用分页片段(pagination_mako.html)]中使用 "page" 来访问 Page object
        context = dict()
        context['keyword'] = keyword
        context['page'] = pager
        html = template.render(**context)
        return HttpResponse(html)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




class BackboneMakoView(View):
    """
    测试 Backbone
    """
    def get(self, request, *args, **kwargs):
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        from mako.template import Template
        template = Template(
            # filename='/home/workspace/medusa/medusaserver/myapp/templates/backbone_model.html',
            filename='/home/workspace/medusa/medusaserver/myapp/templates/backbone_collection.html',
            input_encoding='utf-8',
            output_encoding='utf-8',
        )
        context = {'key': 'value'}
        html = template.render(data=context)
        print html
        return HttpResponse(html)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
