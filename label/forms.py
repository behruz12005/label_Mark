from django import forms

class MyForm(forms.Form):
    CHOICES = (
        (0, '0'),
        (1, '1'),
    )
    my_field = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
