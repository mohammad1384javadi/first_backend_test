from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': 'something@gmail.com',
            'name': 'email'
        }),
        validators=[
            validators.EmailValidator
        ]
    )
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': 'نام شما',
            'name': 'username'
        }),
        validators=[
            validators.MaxLengthValidator(150)
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': '*****',
            'name': 'password'
        }),
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید بیش از ۸ کاراکتر باشد'),
            validators.MaxLengthValidator(20, 'رمز عبور نمی تواند بیش از 20 کاراکتر باشد')
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': '*****',
            'name': 'confirm_password'
        }),
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید بیش از ۸ کاراکتر باشد'),
            validators.MaxLengthValidator(20, 'رمز عبور نمی تواند بیش از 20 کاراکتر باشد')
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        c_pass = self.cleaned_data.get('confirm_password')
        if password == c_pass:
            return c_pass
        raise ValidationError('رمز عبور و تکرار رمز عبور یکسان نیستند')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': 'something@gmail.com',
            'name': 'email'
        }),
        validators=[
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': '*****',
            'name': 'password'
        }),
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید بیش از ۸ کاراکتر باشد'),
            validators.MaxLengthValidator(20, 'رمز عبور نمی تواند بیش از 20 کاراکتر باشد')
        ]
    )


class ForgetPasswordForm(forms.Form):
    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': 'something@gmail.com',
            'name': 'email'
        }),
        validators=[
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': '*****',
            'name': 'username'
        }),
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید بیش از ۸ کاراکتر باشد'),
            validators.MaxLengthValidator(20, 'رمز عبور نمی تواند بیش از 20 کاراکتر باشد')
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 focus:outline-slate-400 rounded-md w-full shadow-sm px-5 py-2',
            'placeholder': '*****',
            'name': 'confirm_password'
        }),
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید بیش از ۸ کاراکتر باشد'),
            validators.MaxLengthValidator(20, 'رمز عبور نمی تواند بیش از 20 کاراکتر باشد')
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        c_pass = self.cleaned_data.get('confirm_password')
        if password == c_pass:
            return c_pass
        raise ValidationError('رمز عبور و تکرار رمز عبور یکسان نیستند')

