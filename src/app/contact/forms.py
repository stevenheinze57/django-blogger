from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
