from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import (UserCreationForm, 
                                    AuthenticationForm, 
                                    UsernameField, 
                                    PasswordChangeForm,
                                    PasswordResetForm,
                                    SetPasswordForm)

class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input-text',
                                                                'placeholder': 'Your Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input-text',
                                                                'placeholder': 'Your Confirm Password'}))
                                                            
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'input-text',
                                            'placeholder': "Your Email Address"}),
            'username': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your Username"}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Password and confirm password doesn't match")
        return password2

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'input-text', 
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input-text',
            'placeholder': 'Your Password'
        }))
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(
        attrs={
            'class': 'input-text',
            'placeholder': 'Your Email Address'
        }))
        
class CustomSetPasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Confirm Your New Password'
                }))

class PasswordChangeCustomForm(PasswordChangeForm):
        old_password = forms.CharField(required=True, label='Old Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your Old Password'
                }))

        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Confirm Your New Password'
                }))

class AccountInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'})
        }
