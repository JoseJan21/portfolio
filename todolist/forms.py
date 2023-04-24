from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tareas

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name','password1', 'password2')


class TareasForm(forms.ModelForm):
    is_done = forms.BooleanField(required=False)

    class Meta:
        model = Tareas
        fields = ['subject', 'description', 'is_done']
