from django.forms import ModelForm
from .models import Display

class DisplayForm(ModelForm):
	class Meta:
		model = Display
		fields = ['date_shown', 'highest_offer', 'status']