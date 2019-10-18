from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.settings import ProfileSetting
from .views.profile import ProfileView
from .views.website import WebSiteView

website = WebSiteView()
profile = ProfileView()
profile_setting = ProfileSetting()

app_name = "website"

urlpatterns = [
    path('', website.home, name="index"),
    path('about/', website.about, name="about"),
    path('contact/', website.contact, name="contact"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('registration/', website.registration, name="registration"),

    # Auth profile route
    path('dashboard/', profile.dashboard, name='dashboard'),
    path('blog-posts/', profile.blog_posts, name='blog-posts'),
    path('comments/', profile.comments, name='comments'),
    path('profile/', profile.profile, name='profile'),
    path('update-profile/', profile.update_profile, name='update-profile'),

    # auth user setting
    path('settings/', auth_views.PasswordChangeView.as_view(template_name='dashboard/settings.html'), name='settings'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
