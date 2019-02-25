from django.shortcuts import render

from .crawling import KyoboCrawler
from .models import SearchList


def index(request):
    searchlist = SearchList.objects.all()
    title = request.GET.get('search', '')
    qs = ''
    if title:
        KyoboCrawler.get_title(title)
        qs = searchlist.filter(title__icontains=title)
    context = {
        'context': qs
    }
    return render(request, 'index.html', context)
