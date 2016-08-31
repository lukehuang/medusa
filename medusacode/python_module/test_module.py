#!/usr/bin/env python
# coding:utf-8

"""
[1] python xxx.py
[2] python -m xxx.py

两种加载py文件的方式:
[1] 直接运行
[2] 相当于import,当做模块来启动

不同的方式加载py文件，主要是影响 __name__ 和 sys.path。
"""
"""
sys.path

    A list of strings that specifies the search path for modules.
    Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

    As initialized upon program startup, the first item of this list, path[0],
    is the directory containing the script that was used to invoke the Python interpreter.
    If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input),
    path[0] is the empty string, which directs Python to search modules in the current directory first.
    Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.
"""

import sys

print __name__
print sys.path

"""
[1] python test_module.py

__main__

['/Users/gaohaoning/VM/workspace/medusa/medusacode/python_module',  # 直接运行,是把py文件所在目录放到了sys.path属性中(第一个位置)
 '/Library/Python/2.7/site-packages/pip-7.1.0-py2.7.egg',
 '/Users/gaohaoning/devstack/xblock_development/xblock-sdk/src/django-pyfs',
 '/Users/gaohaoning/devstack/xblock_development/xblock-sdk',
 '/Users/gaohaoning/devstack/xblock-utils',
 '/Users/gaohaoning/devstack/xblock-work/xblock_conf',
 '/Users/gaohaoning/devstack/XBlock',
 '/Library/Python/2.7/site-packages/Paver-1.2.4-py2.7.egg',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC',
 '/Library/Python/2.7/site-packages']
"""

"""
[2] python -m test_module.py

test_module

['',  # 当做模块来启动,第一个元素是空字符串,表示在当前目录搜索(path[0] is the empty string, which directs Python to search modules in the current directory first.)
 '/Library/Python/2.7/site-packages/pip-7.1.0-py2.7.egg',
 '/Users/gaohaoning/devstack/xblock_development/xblock-sdk/src/django-pyfs',
 '/Users/gaohaoning/devstack/xblock_development/xblock-sdk',
 '/Users/gaohaoning/devstack/xblock-utils',
 '/Users/gaohaoning/devstack/xblock-work/xblock_conf',
 '/Users/gaohaoning/devstack/XBlock',
 '/Library/Python/2.7/site-packages/Paver-1.2.4-py2.7.egg',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC',
 '/Library/Python/2.7/site-packages']
"""
