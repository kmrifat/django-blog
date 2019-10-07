from django.http import HttpResponse
from django.shortcuts import render


class WebSiteView:
    # Create your views here.
    def home(self, request):
        return render(request, "index.html", {})

    def about(self, request):
        return render(request, "about.html", {})

    def contact(self, request):
        return render(request, "contact.html", {})
