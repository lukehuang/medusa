#!/usr/bin/env python
# coding:utf-8

"""
AWS 上线部署脚本(基于 fabric)
    [1] ssh 到目标机器串行执行任务, 一个环节失败后既要显示异常, 又要抛出异常以使得部署行为停止;
    [2] 每个部署子任务的开始、成功结束、异常结束, 都要用颜色显示信息;
"""

import time
import datetime

from fabric.colors import red, yellow, blue, green


class CM(object):
    def __init__(self, func):
        self.func = func
    def __enter__(self):
        print blue('==================================================')
        print blue(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ') + self.func.__name__ + ' : START')
        print blue('==================================================')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'success'):
            if self.success:
                print green('==================================================')
                print green(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ') + self.func.__name__ + ' : SUCCESS')
                print green('==================================================')
            else:
                print red('==================================================')
                print red(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ') + self.func.__name__ + ' : FAIL')
                print red('==================================================')


def show_color(func):
    def wrapper():
        with CM(func) as cm:
            try:
                func()
                cm.success = True
            except Exception, e:
                cm.success = False
                raise e
    return wrapper


@show_color
def test_1():
    print 1/1

@show_color
def test_2():
    print 1/0

if __name__ == '__main__':
    # [1] 前面任务成功,则后面任务可以继续
    test_1()
    time.sleep(1)
    test_2()
    # [2] 前面任务异常,则后面任务不会继续
    # test_2()
    # time.sleep(1)
    # test_1()
