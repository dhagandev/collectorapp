from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

class Gem:
    def __init__(self, gem_type, color, location_found, date_found):
        self.gem_type = gem_type
        self.color = color
        self.location_found = location_found
        self.date_found = date_found

gems = [
    Gem('Turquoise', 'Light Blue', 'Arizona', datetime.datetime(2019, 6, 9)),
    Gem('Quartz', 'Rose Pink', 'South Dakota', datetime.datetime(2019, 5, 23)),
    Gem('Ruby', 'Dark Red', 'Brazil', datetime.datetime(2019, 5, 7)),
    Gem('Malachite', 'Green', 'Mexico', datetime.datetime(2019, 4, 16))
]

def home(request):
    return HttpResponse('<h1>GemCollector</h1>')

def about(request):
    return render(request, 'about.html')

def gems_index(request):
    return render(request, 'gems/index.html', {'gems': gems})