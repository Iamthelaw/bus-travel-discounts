# encoding: utf-8
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'spa_app/index.html', context)