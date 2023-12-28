from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='EMAIL',

        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
            validators.validate_email
        ]
    )
    password = forms.CharField(
        label='PASSWROD',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='CONFIRM PASSWORD',
        widget=forms.PasswordInput(attrs={'placeholder': 'Conform Password'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #
    #     if password == confirm_password:
    #         return False
    #
    #     return True