from django.http import HttpResponse
from django.shortcuts import render

from editor.models import Page


def home(request):
    page = Page.objects.get(pk=1)
    return render(request, 'home.html', {'page': page, 'editable': True})


def update_page(request, title):
    page = Page.objects.get(title=title)
    param_keys = request.POST.keys()
    for key in param_keys:
        page.content[key] = request.POST[key]
    page.save()
    
    return HttpResponse("--- Page saved successfully ---")


def about(request):
    return render(request, 'about.html')
