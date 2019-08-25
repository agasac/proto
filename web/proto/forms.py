from django import forms
from .models import Prefecture, Spot

class SpotSearchForm(forms.Form):
    prefecture = forms.ModelChoiceField(
        queryset=Prefecture.objects, label='都道府県', required=False
    )

class JaranSearchForm(forms.Form):
    pref_choices = [('東京都','東京都'), ('大阪府','大阪府')]
    prefecture = forms.ChoiceField(label='都道府県', choices=pref_choices, required=True)
