from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',
        required=True,
        help_text='Имя не должно содержать: @, /, _, &',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        label='',
        required=True,
        help_text='Почта должна быть актуальной',
        widget=forms.TextInput(attrs={'placeholder': 'Введите почту'})
    )

    password1 = forms.CharField(
        label='',
        required=True,
        help_text='Пароль не должен быть простым',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

    password2 = forms.CharField(
        label='',
        required=True,
        help_text='Пароли должны совпадать',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Логин для обновления'})
    )

    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Почта для обновления'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
