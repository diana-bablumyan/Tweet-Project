from .models import Email
from django import forms

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ['date_send']