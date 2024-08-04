from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
   #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}
    Email = forms.EmailField(label="Email Address", required=True)
    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')