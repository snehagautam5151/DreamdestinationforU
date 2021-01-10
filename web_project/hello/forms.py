from django import forms
from .models import Contact


class ContactCreate(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ["name", "email", "address","state", "phone","zip"]
       