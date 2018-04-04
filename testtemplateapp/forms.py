from django import forms

class FeedForm(forms.Form):
    firstname = forms.CharField(label="Есімі", max_length=50)
    lastname = forms.CharField(label="Тегі", max_length=50)
    email = forms.EmailField(label="email")