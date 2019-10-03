from django import forms
from django.forms import ModelForm,TextInput
from .models import Post, Profile, Comment
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': "form-control",'placeholder':"Enter Your UserName"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':"Enter Your Password  "}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': "form-control"}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': "form-control"}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets={'username':TextInput(attrs={'class':"form-control"}),
        'first_name':TextInput(attrs={'class':"form-control"}),
        'last_name':TextInput(attrs={'class':"form-control"}),
        'email':TextInput(attrs={'class':"form-control"}),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)



class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
