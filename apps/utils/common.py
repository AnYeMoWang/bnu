# coding: utf-8
# author: h.shi
# 一些通用的函数
import json
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse

_PER_PAGE = 10


class JSONHttpResponse(HttpResponse):

    """ Make a response in JSON format """

    def __init__(self, content='', callback='', pretty=False, *args, **kwargs):
        super(HttpResponse, self).__init__(
            content_type="application/json", *args, **kwargs)

        if pretty:
            options = {'indent': 8, 'separators': (',', ': ')}
        elif settings.DEBUG:
            options = {'indent': 4, 'separators': (',', ': ')}
        else:
            options = {'separators': (',', ':')}

        self.content = json.dumps(content, **options)

        if callback:
            if re.match(r'^\w$', callback):
                raise ValueError('Invalid callback')
            else:
                self.content = '%s(%s)' % (callback, self.content)


def _paginator_result(queryset, page, per_page=10):
    # paginator function
    paginator = Paginator(queryset, per_page)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)
    return results


# 获取request header中的ip地址
def get_ip(request):
    HEADER_FIELDS = [
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_REAL_FORWARDED_FOR',
        'HTTP_CLIENT_IP',
        'REMOTE_ADDR',
        'X-Real-IP',
    ]
    for header in HEADER_FIELDS:
        ip = request.META.get(header, '')
        if ip:
            break
    return ip
