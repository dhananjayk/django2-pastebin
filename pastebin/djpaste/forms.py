from django import forms

SYNTAX_CHOICES = (
    ('', ''),
    ('css', 'CSS'),
    ('javascript', 'JavaScript'),
    ('python', 'Python'),
)


class PasteForm(forms.Form):
    text = forms.CharField(label='New Paste', widget=forms.Textarea(attrs={'rows': '10', 'class': 'form-control'}))
    paste_name = forms.CharField(label='Paste Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    paste_expiration = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    private_paste = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    syntax_highlighting = forms.ChoiceField(choices=SYNTAX_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))