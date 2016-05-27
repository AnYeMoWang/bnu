from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from bnu.views import index
from django.conf import settings

from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = [
    url(r'^!bnu404~', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^index$', index),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^practice/', include('apps.practice.urls')),
    url(r'^trade/', include('apps.trade.urls')),
    url(r'^share/', include('apps.share.urls')),
    url(r'^uploads$', include('apps.uploads.urls')),
    url(
        r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
    url(
        r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
    )
]

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^403', TemplateView.as_view(template_name='403.html')),
        url(r'^404', TemplateView.as_view(template_name='404.html')),
        url(r'^500', TemplateView.as_view(template_name='500.html')),
    )
