from django.shortcuts import render

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    return render(request, 'women/index.html', {'title': 'Django'})


def about(request):
    menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
    return render(request, 'women/about.html', {'menu': menu, 'title': "О приложении"})


def posts(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})
