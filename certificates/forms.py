# certificates/forms.py
from django import forms

class CertificateSearchForm(forms.Form):
    certificate_number = forms.CharField(max_length=13, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter Certificate Number',
        'class': 'form-control',
    }))
