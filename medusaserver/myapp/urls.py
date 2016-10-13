# coding: utf-8

from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    # 新闻列表
    url('^news/$', views.NewsListView.as_view(), name='news_list'),

    # 对于无法直接通过HTTP请求下载的资源,添加下载代理通过requests获取资源后修改header来实现浏览器下载
    url(r'^test/download/$', views.DownloadView.as_view(), name='download'),

    # 渲染模板
    url('^test/template/$', views.TestTemplateView.as_view(), name='test_template'),
    # echarts 显示树状结构
    url('^test/tree/$', views.TreeView.as_view(), name='tree'),

    # 测试 Sentry ( Raven captureException & captureMessage )
    url('^test/sentry/$', views.SentryTestView.as_view(), name='sentry_test'),
    # 测试 Sentry ( Raven installed a hook in Django that will automatically report uncaught exceptions )
    url('^test/exception/$', views.ExceptionTestView.as_view(), name='exception_test'),
    # 测试 Sentry ( Sentry Log )
    url('^test/sentry_log/$', views.SentryLogTestView.as_view(), name='sentry_log_test'),

    # 测试 Django process thread
    url('^thread/$', views.ProcessThreadView.as_view(), name='test_process_thread'),

    # 测试 rsyslog
    url('^rsyslog/$', views.RsyslogView.as_view(), name='test_rsyslog'),
]
