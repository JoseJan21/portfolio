from django import forms
from django.core import validators

from django.contrib.auth.forms import   UserCreationForm
from django.contrib.auth.models import User
from blog.models import Article
# from todolist.models import Routine

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name','password1', 'password2')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'categories']