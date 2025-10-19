from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject of your message'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'How can we help you?',
                'rows': 5
            }),
        }