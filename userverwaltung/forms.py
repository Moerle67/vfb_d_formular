# forms.py
from django import forms
from .models import *

class BenutzerForm(forms.ModelForm):

    class Meta:
        model = Benutzer
        widgets = {
           'password': forms.PasswordInput(),
        }