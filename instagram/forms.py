from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Comment, Profile


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PostPictureForm(forms.ModelForm):
    model = Post