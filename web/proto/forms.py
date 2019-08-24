from django import forms
from .models import Prefecture, Spot

class SpotSearchForm(forms.Form):
    prefecture = forms.ModelChoiceField(
        queryset=Prefecture.objects, label='都道府県', required=False
    )
