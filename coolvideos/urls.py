from django.conf.urls import patterns, include, url
from django.contrib import admin
from videos import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.VideosIndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mojam/', include('videos.urls', namespace='videos')),

    url(r'^admin/', include(admin.site.urls)),
)
