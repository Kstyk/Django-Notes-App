from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter email...'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter first name...'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter last name...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Enter password...'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input input-bordered w-full rounded-none focus:outline-none focus:border-gray-600', 'placeholder': 'Confirm password...'}))

    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name', 'password', 'confirm_password'
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password
