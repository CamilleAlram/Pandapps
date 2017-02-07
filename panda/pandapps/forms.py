from django import forms
# from django.forms.utils import ErrorList
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['mail', 'sujet', 'nom', 'prenom', 'pseudo', 'message']
