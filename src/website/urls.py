from django.urls import path

from .views import WebSiteView

website = WebSiteView()

app_name = "website"

urlpatterns = [
    path('', website.home, name="index"),
    path('about/', website.about, name="about"),
    path('contact/', website.contact, name="contact"),
]
