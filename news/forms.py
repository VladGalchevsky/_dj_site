from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from captcha.fields import CaptchaField
from .models import News
import re


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не має починатися з цифри')
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Імʼя користувача', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Електронна пошта', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Підтвердження пароля', widget=forms.PasswordInput(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Імʼя користувача', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    captcha = CaptchaField()
