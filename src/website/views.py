from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .form.registration import UserRegisterForm
from .models import Contact
from .form.contact import ContactForm


class WebSiteView:
    # Create your views here.
    def home(self, request):

        return render(request, "index.html", {'home': True})

    def about(self, request):
        return render(request, "about.html", {})

    def contact(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # print(form.cleaned_data['full_name'])
                contact = Contact.objects.create(**form.cleaned_data)
                messages.success(request, 'Thank you')
                return redirect('/contact/')
        else:
            form = ContactForm()
            return render(request, "contact.html", {'form': form})

    def login(self, request):
        return render(request, "login.html", {})

    def registration(self, request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account Created for {username}')
                return redirect('website:registration')
        else:
            form = UserRegisterForm()
        return render(request, "registration.html", {'form': form})
