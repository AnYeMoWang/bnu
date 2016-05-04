from django.shortcuts import render
from .models import Practice


def index(request):
    current_type = request.GET.get('type', 'all')
    path = u'practice'
    type_choices = Practice.type_choices
    choices = []
    int_type = 0
    for tc in type_choices:
        if tc[1] == current_type:
            int_type = tc[0]
        choices.append(tc[1])
    if not int_type:
        current_type = u'all'
    practices = Practice.objects.filter(type=int_type).order_by('submit_time')
    resp = {
        'article': practices,
        'choices': choices,
        'current_type': current_type,
        'path': path,
    }
    return render(request, 'practice/index.html', resp)
