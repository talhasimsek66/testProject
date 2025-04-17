from django import forms

class PublisherForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))