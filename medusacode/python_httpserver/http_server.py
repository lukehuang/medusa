#!/usr/bin/env python
# coding:utf-8

"""
Python HTTPServer
"""

# ====================================================================================================
"""
The SimpleHTTPServer module can be invoked directly using the -m switch of the interpreter with a port number argument.
This serves the files relative to the current directory.
"""
"""
Python内置了一个简单的HTTP服务器，只需要在命令行下面敲一行命令，一个HTTP服务器就起来了：
这个服务会将当前所在的文件夹设置为默认的Web目录。
如果当前文件夹有index.html文件则会默认显示该文件，否则会以文件列表的形式显示目录下所有文件。
"""

# python -m SimpleHTTPServer 8000
# ====================================================================================================
"""
The SimpleHTTPServer module can be used in the following manner
in order to set up a very basic web server serving files relative to the current directory.
"""
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
# ====================================================================================================

