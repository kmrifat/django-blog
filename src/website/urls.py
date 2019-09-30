from django.urls import path

from .views import WebSiteView

website = WebSiteView()

urlpatterns = [
    path('', website.home),
    path('about/', website.about),
    path('contact/', website.contact),
]
