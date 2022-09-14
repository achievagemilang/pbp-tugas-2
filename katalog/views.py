from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

list_katalog = CatalogItem.objects.all()
context = {
    'list_katalog': list_katalog,
    'name': 'Achieva Futura Gemilang',
    'student_id': '2106750452'
}

def show_katalog(request):
    return render(request, "katalog.html", context)