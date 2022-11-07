from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

    username = forms.CharField(label="Username ")
    email = forms.EmailField(label="Email ")
    password1 = forms.CharField(label="Password ", widget=forms.PasswordInput, min_length=8,  
        help_text="Contains at least 8 characters and password cannot be entirely numeric.") 
    password2 = forms.CharField(label="Re-enter Password ", widget=forms.PasswordInput,  min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email' : None, 
        }