from django import forms
from .models import CarConfiguration

class CarConfigurationForm(forms.ModelForm):
    class Meta:
        model = CarConfiguration
        fields = ['color', 'wheels', 'interior']
        widgets = {
            'color': forms.RadioSelect(attrs={'class': 'color-option'}),
            'wheels': forms.RadioSelect(),
            'interior': forms.RadioSelect(),
        }