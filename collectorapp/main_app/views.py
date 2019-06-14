from django.shortcuts import render
from django.http import HttpResponse
from .models import Gem
# Create your views here.

def home(request):
    return HttpResponse('<h1>GemCollector</h1>')

def about(request):
    return render(request, 'about.html')

def gems_index(request):
    gems = Gem.objects.all()
    return render(request, 'gems/index.html', {'gems': gems})

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    return render(request, 'gems/detail.html', {'gem': gem})