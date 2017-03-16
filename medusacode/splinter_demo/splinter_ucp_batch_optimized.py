#!/usr/bin/env python
# coding:utf-8

from splinter import Browser

URL_UCAMPUS = 'http://rmdx.testucampus.unipus.cn'
URL_UCAMPUS_BIND = 'http://rmdx.testucampus.unipus.cn/toBingding?school_id=8225'

data = [
    # ['ucptest2107', 'pass2107', 1000002, u'赵二'],
    # ['ucptest2108', 'pass2108', 1000003, u'赵三'],
    # ['ucptest2109', 'pass2109', 1000004, u'赵四']
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

    import time
    time.sleep(1)

    browser.visit(URL_UCAMPUS_BIND)

    input_num = browser.find_by_name('num')
    input_name = browser.find_by_name('name')
    input_num[0].fill(info[2])
    input_name[0].fill(info[3])

    btn_commit = browser.find_by_id('studenBtn')
    btn_commit.click()

    print 'completed: %s' % str(info)

    time.sleep(1)
    browser.quit()
