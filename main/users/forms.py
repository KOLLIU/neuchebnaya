from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "autocomplete": "new-password"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "autocomplete": "new-password"}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    # pass

# class CharacterForm(forms.ModelForm):
#     class Meta:
#         model = Character
#         # fields = "__all__"
#         fields = ["name", "role", "description"]
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "role": forms.TextInput(attrs={"class": "form-control"}),
#             "description": forms.Textarea(attrs={"class": "form-control", "rows": 5})
#         }
