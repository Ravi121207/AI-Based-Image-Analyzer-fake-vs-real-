from django import forms
from django.contrib.auth.models import User
from .models import ImageUpload

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ['image']
