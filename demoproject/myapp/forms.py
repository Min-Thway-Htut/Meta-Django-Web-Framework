from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea)
