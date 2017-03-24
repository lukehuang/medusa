#!/usr/bin/env python
# coding:utf-8

import time
import logging
import sys

from splinter import Browser

logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s [%(message)s]')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# URL_UCAMPUS = 'http://rmdx.testucampus.unipus.cn'
URL_UCAMPUS = 'http://trial.ucampus.unipus.cn'

data = [
    # ['ucptest2107', 'pass2107', 1000002, u'赵二'],
    # ['ucptest2108', 'pass2108', 1000003, u'赵三'],
    # ['ucptest2109', 'pass2109', 1000004, u'赵四'],
    # ['ucptest2110', 'pass2110', 1000005, u'赵五'],
    # ['ucptest2111', 'pass2111', 1000006, u'赵️六'],
]

data = [
    # ['tch0001', 'ucampus123', 170001, u'teacher'],
    # ['tch0002', 'ucampus123', 170002, u'teacher'],
    # ['tch0003', 'ucampus123', 170003, u'teacher'],
    # ['tch0004', 'ucampus123', 170004, u'teacher'],
    # ['tch0005', 'ucampus123', 170005, u'teacher'],
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
        # 教师账号需要点击span切换tab, 学生账号不需要
        tab = iframe.find_by_text('我是老师')
        tab.click()

        input_num = iframe.find_by_id('teachenum')
        input_name = iframe.find_by_id('teachename')
        # input_num = iframe.find_by_id('studentnum')
        # input_name = iframe.find_by_id('studentname')

        input_num[0].fill(info[2])
        input_name[0].fill(info[3])
        btn_commit = iframe.find_by_id('teachBtn')
        # btn_commit = iframe.find_by_id('studenBtn')

        # btn_commit.click()  # !!!!!!!!!!!!!!!!!!!!!!!!!
        # btn_commit.right_click()

    info = 'completed: %s' % str(info)
    print info
    logger.info(info)

    # time.sleep(1)
    browser.quit()
