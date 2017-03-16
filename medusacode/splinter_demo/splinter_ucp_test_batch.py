#!/usr/bin/env python
# coding:utf-8

import time
from splinter import Browser

URL_UCAMPUS = 'http://rmdx.testucampus.unipus.cn'

data = [
    # ['ucptest2107', 'pass2107', 1000002, u'赵二'],
    # ['ucptest2108', 'pass2108', 1000003, u'赵三'],
    # ['ucptest2109', 'pass2109', 1000004, u'赵四'],
    # ['ucptest2110', 'pass2110', 1000005, u'赵五'],
    # ['ucptest2111', 'pass2111', 1000006, u'赵️六'],
]


for info in data:
    browser = Browser('chrome')
    browser.visit(URL_UCAMPUS)
    btn_login = browser.find_by_text("登录")
    btn_login.click()

    input_username = browser.find_by_name('username')
    input_password = browser.find_by_name('password')
    input_username[0].fill(info[0])
    input_password[0].fill(info[1])
    btn_login = browser.find_by_id("login")
    btn_login.click()

    # 由于原网页的 iframe 延迟渲染,需要等待一下才能使用 get_iframe 方法:
    time.sleep(1)
    with browser.get_iframe('layui-layer-iframe1') as iframe:
        input_num = iframe.find_by_name('num')
        input_name = iframe.find_by_name('name')
        input_num[0].fill(info[2])
        input_name[0].fill(info[3])
        btn_commit = iframe.find_by_id('studenBtn')
        btn_commit.click()  # !!!!!!!!!!!!!!!!!!!!!!!!!

    print 'completed: %s' % str(info)

    time.sleep(1)
    browser.quit()
