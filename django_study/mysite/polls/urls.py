from django.conf.urls import patterns,url
import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<poll_id>\d+)/result/$', views.result, name='result'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

