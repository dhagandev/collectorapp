from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem, Emotion
from .forms import DisplayForm
# Create your views here.

class GemCreate(LoginRequiredMixin, CreateView):
    model = Gem
    fields = ['gem_type', 'color', 'location_found', 'date_found']
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class GemUpdate(LoginRequiredMixin, UpdateView):
    model = Gem
    fields = ['gem_type', 'color', 'location_found', 'date_found']

class GemDelete(LoginRequiredMixin, DeleteView):
    model = Gem
    success_url = '/gems/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def gems_index(request):
    gems = Gem.objects.filter(user=request.user)
    return render(request, 'gems/index.html', {'gems': gems})

@login_required
def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    display_form = DisplayForm()
    emotions_gem_not_have = Emotion.objects.exclude(
        id__in=gem.emotions.all().values_list('id'))
    return render(request, 'gems/detail.html', {
        'gem': gem,
        'display_form': display_form,
        'emotions': emotions_gem_not_have
    })

def add_display(request, gem_id):
    form = DisplayForm(request.POST)
    if form.is_valid():
        new_display = form.save(commit=False)
        new_display.gem_id = gem_id
        new_display.save()
    return redirect('detail', gem_id = gem_id)

@login_required
def assoc_emotion(request, gem_id, emotion_id):
  Gem.objects.get(id=gem_id).emotions.add(emotion_id)
  return redirect('detail', gem_id=gem_id)

@login_required
def unassoc_emotion(request, gem_id, emotion_id):
  Gem.objects.get(id=gem_id).emotions.remove(emotion_id)
  return redirect('detail', gem_id=gem_id)

class EmotionList(LoginRequiredMixin, ListView):
  model = Emotion

class EmotionDetail(LoginRequiredMixin, DetailView):
  model = Emotion

class EmotionCreate(LoginRequiredMixin, CreateView):
  model = Emotion
  fields = '__all__'

class EmotionUpdate(LoginRequiredMixin, UpdateView):
  model = Emotion
  fields = '__all__'

class EmotionDelete(LoginRequiredMixin, DeleteView):
    model = Emotion
    success_url = '/emotions/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)