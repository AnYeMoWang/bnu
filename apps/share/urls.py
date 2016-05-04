from django.conf.urls import patterns, url
from apps.share import views

urlpatterns = patterns('',
                       url(r'^$', views.lesson),
                       url(r'^lesson/$', views.lesson),
                       url(r'^lesson/child/(?P<parent_id>[\d]+?)$',views.child_lesson),
                       url(r'^exercise/$', views.exercise),
                       url(r'^datum/$', views.doc),
                       url(r'^datum/doc/$', views.doc),
                       url(r'^datum/frame/$', views.frame),
                       url(r'^datum/frame/article$', views.article),
                       url(r'^downloads/$', views.downloads),
                       )
