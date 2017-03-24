#!/usr/bin/env python
# coding=utf-8


from math import hypot
from random import random
import time
import os
import thread
import logging
from multiprocessing import Pool
from splinter import Browser

logger = logging.getLogger('student_logger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('student_log.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(levelname)s %(asctime)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s [%(message)s]')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# URL_UCAMPUS = 'http://rmdx.testucampus.unipus.cn'
URL_UCAMPUS = 'http://trial.ucampus.unipus.cn'

# data_list = [
#     ['stu0001', 'ucampus123', 201700001, 'studenta'],
#     ['stu0002', 'ucampus123', 201700002, 'studentb'],
#     ['stu0003', 'ucampus123', 201700003, 'studentc'],
#     ['stu0004', 'ucampus123', 201700004, 'studentd'],
#     ['stu0005', 'ucampus123', 201700005, 'studente'],
#     ['stu0006', 'ucampus123', 201700006, 'studentf'],
#     ['stu0007', 'ucampus123', 201700007, 'studentg'],
#     ['stu0008', 'ucampus123', 201700008, 'studenth'],
#     ['stu0009', 'ucampus123', 201700009, 'studenti'],
#     ['stu0010', 'ucampus123', 201700010, 'studentj'],
#     ['stu0011', 'ucampus123', 201700011, 'studenta'],
#     ['stu0012', 'ucampus123', 201700012, 'studentb'],
#     ['stu0013', 'ucampus123', 201700013, 'studentc'],
#     ['stu0014', 'ucampus123', 201700014, 'studentd'],
#     ['stu0015', 'ucampus123', 201700015, 'studente'],
#     ['stu0016', 'ucampus123', 201700016, 'studentf'],
#     ['stu0017', 'ucampus123', 201700017, 'studentg'],
#     ['stu0018', 'ucampus123', 201700018, 'studenth'],
#     ['stu0019', 'ucampus123', 201700019, 'studenti'],
#     ['stu0020', 'ucampus123', 201700020, 'studentj'],
# ]

from student_data import data_list


def work(info):
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
    try:
        with browser.get_iframe('layui-layer-iframe1') as iframe:
            # 教师账号需要点击span切换tab, 学生账号不需要
            # tab = iframe.find_by_text('我是老师')
            # tab.click()

            # input_num = iframe.find_by_id('teachenum')
            # input_name = iframe.find_by_id('teachename')
            input_num = iframe.find_by_id('studentnum')
            input_name = iframe.find_by_id('studentname')

            input_num[0].fill(info[2])
            input_name[0].fill(info[3])
            # btn_commit = iframe.find_by_id('teachBtn')
            btn_commit = iframe.find_by_id('studenBtn')

            btn_commit.click()  # !!!!!!!!!!!!!!!!!!!!!!!!!
            # btn_commit.right_click()

        msg = 'completed: %s' % str(info)
        print msg
        logger.info(msg)
        time.sleep(1)
        browser.quit()
    except Exception:
        msg = 'error: %s' % str(info)
        print msg
        logger.error(msg)
        time.sleep(1)
        browser.quit()



def batch_work(item_list):
    # ------------------------------------------------------------------------------------------
    pool = Pool(8)
    result = pool.map(work, item_list)  # 进程池
    # ------------------------------------------------------------------------------------------
    return result


batch_work(data_list)
