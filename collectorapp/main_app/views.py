from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem
from .forms import DisplayForm
# Create your views here.

class GemCreate(CreateView):
    model = Gem
    fields = '__all__'

class GemUpdate(UpdateView):
    model = Gem
    fields = '__all__'

class GemDelete(DeleteView):
    model = Gem
    success_url = '/gems/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gems_index(request):
    gems = Gem.objects.all()
    return render(request, 'gems/index.html', {'gems': gems})

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    display_form = DisplayForm()
    return render(request, 'gems/detail.html', {
        'gem': gem, 
        'display_form': display_form
    })

def add_display(request, gem_id):
    form = DisplayForm(request.POST)
    if form.is_valid():
        new_display = form.save(commit=False)
        new_display.gem_id = gem_id
        new_display.save()
    return redirect('detail', gem_id = gem_id)