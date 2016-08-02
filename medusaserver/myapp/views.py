#!/usr/bin/env python
# coding: utf-8

import os
import datetime
import random

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
