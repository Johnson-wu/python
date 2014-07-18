#coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
# import polls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/',include('polls.urls', namespace='polls')),
    # url(r'^polls/',include(polls.urls)),	# 加引号与不加引号有什么区别？
)
