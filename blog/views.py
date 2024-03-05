from django.shortcuts import render
from django.http import HttpResponse


def portao(request):
    return render(request, 'blog/porta.html', {})


def sala(request):
    return HttpResponse('Você chegou na sala. Senta no sofá')


def quarto(request):
    return HttpResponse('Agora está no quarto, pode se deitar.')


def post_list(request):
    return render(request, 'blog/post_list.html', {})

