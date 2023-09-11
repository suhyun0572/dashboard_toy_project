from django import forms
from .models import trailers

# class TrailerForm(forms.Form) :
#     plate = forms.CharField(max_length=8)
#     location = forms.CharField(max_length=8)
#     company = forms.CharField(max_length=15)

class TrailerForm(forms.ModelForm):
    class Meta:
        model = trailers
        fields = ('plate','location','company',)
    