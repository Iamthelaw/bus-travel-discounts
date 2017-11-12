"""Index view for app."""
from django.shortcuts import render


def index(request):
    """Index view."""
    context = {}
    return render(request, 'spa_app/index.html', context)
