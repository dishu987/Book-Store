from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'custom-input','placeholder':'Password1...'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'custom-input','placeholder':'Password2...'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'custom-input','placeholder':'Email...'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'custom-input','placeholder':'Username...'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'custom-input','placeholder':'username...'}))
    password = forms.CharField(label=_("Passowrd"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'custom-input','placeholder':'password...'}))