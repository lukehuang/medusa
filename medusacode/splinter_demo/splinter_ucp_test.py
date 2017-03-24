#!/usr/bin/env python
# coding:utf-8

from splinter import Browser


browser = Browser('chrome')
browser.visit('http://rmdx.testucampus.unipus.cn')

btn_login = browser.find_by_text("登录")
btn_login.click()

input_username = browser.find_by_name('username')
input_password = browser.find_by_name('password')
input_username[0].fill('ucptest2115')
input_password[0].fill('pass2115')
btn_login = browser.find_by_id("login")
btn_login.click()

# 由于原网页的 iframe 延迟渲染,需要等待一下才能使用 get_iframe 方法:
import time
time.sleep(1)

with browser.get_iframe('layui-layer-iframe1') as iframe:
    input_num = iframe.find_by_name('num')
    input_name = iframe.find_by_name('name')
    input_num[0].fill('1000004')
    input_name[0].fill(u'赵四')
    btn_commit = iframe.find_by_id('studenBtn')
    print btn_commit
    # btn_commit.click()  # !!!!!!!!!!!!!!!!!!!!!!!!!

time.sleep(1)
browser.quit()
