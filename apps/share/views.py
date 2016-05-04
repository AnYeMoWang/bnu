from django.shortcuts import render
from django.shortcuts import get_object_or_404
from apps.utils.common import _paginator_result
from apps.share.models import ParentLessons, ChildLessons, Frame, Doc, Downloads, Exercise


def lesson(request):
    current_type = 'lesson'
    page = request.GET.get('page', 1)
    queryset = ParentLessons.objects.all().order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=9)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/lesson.html', resp)


def child_lesson(request, parent_id):
    current_type = 'lesson'
    page = request.GET.get('page', 1)
    queryset = ChildLessons.objects.filter(
        parent__id=parent_id
    ).order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=15)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/child_lesson.html', resp)


def exercise(request):
    current_type = 'exercise'
    page = request.GET.get('page', 1)
    queryset = Exercise.objects.all().order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=10)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/exercise.html', resp)


def doc(request):
    current_type = 'datum'
    current_inner = 'doc'
    page = request.GET.get('page', 1)
    queryset = Doc.objects.all().order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=10)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'current_inner': current_inner,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/doc.html', resp)


def frame(request):
    current_type = 'datum'
    current_inner = 'frame'
    page = request.GET.get('page', 1)
    queryset = Frame.objects.all().order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=10)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'current_inner': current_inner,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/frame.html', resp)


def article(request):
    current_type = 'datum'
    current_inner = 'frame'
    article_id = request.GET.get('id', None)
    article = get_object_or_404(Frame, id=article_id)
    article.has_viewed()
    resp = {
        'article': article,
        'current_type': current_type,
        'current_inner': current_inner,
    }
    return render(request, 'share/article.html', resp)


def downloads(request):
    current_type = 'downloads'
    page = request.GET.get('page', 1)
    queryset = Downloads.objects.all().order_by('-submit_time')
    result = _paginator_result(queryset, page, per_page=15)
    page_max_show = 10
    resp = {
        'result': result,
        'current_type': current_type,
        'paginator': {
            'page_show_max': (int(page) + page_max_show / 2),
            'page_show_min': (int(page) - page_max_show / 2),
            'page': page,
        }
    }
    return render(request, 'share/downloads.html', resp)
