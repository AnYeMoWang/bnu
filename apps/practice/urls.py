from django.conf.urls import patterns, url
from apps.practice import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'index/', views.index),
                       )
