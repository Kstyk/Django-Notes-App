from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import login, authenticate, logout


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter email...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter password...'}))

    class Meta:
        model = CustomUser
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter email...'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter first name...'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter last name...'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter password...'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Confirm password...'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']
