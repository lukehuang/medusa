#!/usr/bin/env python
# coding:utf-8

from splinter import Browser


browser = Browser('chrome')
browser.visit('http://rmdx.testucampus.unipus.cn')

btn_login = browser.find_by_text("登录")
btn_login.click()

input_username = browser.find_by_name('username')
input_password = browser.find_by_name('password')
input_username[0].fill('ucptest2107')
input_password[0].fill('pass2107')
btn_login = browser.find_by_id("login")
btn_login.click()

import time
time.sleep(1)

browser.visit('http://rmdx.testucampus.unipus.cn/toBingding?school_id=8225')

input_num = browser.find_by_name('num')
input_name = browser.find_by_name('name')
input_num[0].fill('1000002')
input_name[0].fill(u'赵二')

btn_commit = browser.find_by_id('studenBtn')
print btn_commit
# btn_commit.click()  # !!!!!!!!!!!!!!!!!!!!!!!!!

time.sleep(1)
browser.quit()
