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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']

    def save(self, user=None):
        profile = super(UserCreateForm, self).save(commit=False)
        if user:
            profile.user = user
        profile.save()
        return profile


class PostPictureForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption',  'date_posted', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)       




