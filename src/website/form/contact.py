from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label='Enter your name', max_length=100)
    email_address = forms.EmailField(label='Enter your email', max_length=100)
    phone_number = forms.CharField(label='Enter phone number', max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    full_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Your Name'})
    email_address.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Email Address'})
    phone_number.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Phone Number'})
    message.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Message', 'rows': '5'})
