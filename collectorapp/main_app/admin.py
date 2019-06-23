from django.contrib import admin
from .models import Gem, Display, Emotion

# Register your models here.
admin.site.register(Gem)
admin.site.register(Display)
admin.site.register(Emotion)