from django import forms


class ChangeEmailAddress(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}), required=True)
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Current Password'}), required=True)


class ChangeUsername(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}), required=True)
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Current Password'}), required=True)
