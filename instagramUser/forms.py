from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Profile
from instagram.models import Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username','email','first_name','password1','password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('username','password1')



class UserProfilForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email','password', 'bio','img')


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','img','tags','location')