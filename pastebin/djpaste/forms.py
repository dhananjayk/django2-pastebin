from django import forms


class PasteForm(forms.Form):
    text = forms.CharField(label='New Paste',  widget=forms.Textarea(attrs={'rows': '10', 'class': 'form-control'}))
