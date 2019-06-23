from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem, Emotion
from .forms import DisplayForm
# Create your views here.

class GemCreate(CreateView):
    model = Gem
    fields = ['gem_type', 'color', 'location_found', 'date_found']

class GemUpdate(UpdateView):
    model = Gem
    fields = ['gem_type', 'color', 'location_found', 'date_found']

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

def assoc_emotion(request, gem_id, emotion_id):
  Gem.objects.get(id=gem_id).emotions.add(emotion_id)
  return redirect('detail', gem_id=gem_id)

def unassoc_emotion(request, gem_id, emotion_id):
  Gem.objects.get(id=gem_id).emotions.remove(emotion_id)
  return redirect('detail', gem_id=gem_id)

class EmotionList(ListView):
  model = Emotion

class EmotionDetail(DetailView):
  model = Emotion

class EmotionCreate(CreateView):
  model = Emotion
  fields = '__all__'

class EmotionUpdate(UpdateView):
  model = Emotion
  fields = '__all__'

class EmotionDelete(DeleteView):
    model = Emotion
    success_url = '/emotions/'