from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'our_resume/main.html')

def pageNotFound(request,exception):
    return HttpResponseNotFound(render(request, 'our_resume/404game.html'))
