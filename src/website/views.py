from django.http import HttpResponse
from django.shortcuts import render


class WebSiteView:
    # Create your views here.
    def home(self, request):
        return render(request, "website/index.html", {})

    def about(self, request):
        return HttpResponse('<h1>About Us</h1>')

    def contact(self, request):
        return HttpResponse('<h1>Contact</h1>')
