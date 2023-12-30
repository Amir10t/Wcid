from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
            validators.validate_email
        ]
    )
    password = forms.CharField(
        label='گذرواژه',
        widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار گذرواژه',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}),
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