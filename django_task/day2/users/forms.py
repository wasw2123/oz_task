from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ('password1', 'password2'):
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'password'
            if self.fields[field] == "password1":
                self.fields[field].label = '비밀번호'
            if self.fields[field] == "password2":
                self.fields[field].label = '비밀번호 확인'


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name', 'email']
        labels = {
            'name': '이름',
            'email': '이메일',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '이메일'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].label = '비밀번호'
        self.fields['password'].widget.attrs['class'] = 'form-control'
