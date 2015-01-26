from django.conf.urls import patterns, url

#Mojam URLS

from . import views

urlpatterns = patterns('',
	#url(r'^$', views.TermListView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.VideoDetailView.as_view(), name='video_detail'),
	)
