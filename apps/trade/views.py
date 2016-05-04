from django.shortcuts import render
from django.shortcuts import get_object_or_404
from apps.utils.common import _paginator_result
from apps.trade.models import Trade


def index(request):
    modal = Trade
    path = u'trade'
    current_type = request.GET.get('type', 'all')
    page = request.GET.get('page', 1)
    type_choices = modal.type_choices
    choices = []
    int_type = 0
    for tc in type_choices:
        if tc[1] == current_type:
            int_type = tc[0]
        choices.append(tc[1])
    if not int_type:
        current_type = u'all'
        queryset = modal.objects.all().order_by('-submit_time')
    else:
        queryset = modal.objects.filter(
            type=int_type
        ).order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=15)
    page_max_show = 10
    resp = {
        'result': result,
        'choices': choices,
        'current_type': current_type,
        'path': path,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'trade/index.html', resp)


def article(request):
    modal = Trade
    path = u'trade'
    article_id = request.GET.get('id', None)
    article = get_object_or_404(modal, id=article_id)
    article.has_viewed()
    type_choices = modal.type_choices
    resp = {
        'article': article,
        'path': path,
        'current_type': article.get_type_display(),
        'choices': [i[1] for i in type_choices],
    }
    return render(request, 'trade/article.html', resp)
