from django import forms

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Name", widget=forms.TextInput(attrs={"placeholder": "Nutzername / Email"}))
    password = forms.CharField(label="Passwort", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


