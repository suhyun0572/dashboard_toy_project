from django.forms import forms
from .models import trailers

class TrailerForm(forms.Form) :
    class Meta:
        model = trailers
        fields = ['plate','location','company']
    