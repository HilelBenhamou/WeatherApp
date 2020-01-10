from django import forms


class MeteoForm(forms.Form):
    city = forms.CharField(label='Choose your City  ', widget= forms.TextInput(attrs={'placeholder':'Paris or Tel aviv'}), max_length=100)