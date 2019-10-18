from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from ..form.settings import ChangeUsername
from ..form.settings import ChangeEmailAddress
from ..form.registration import ProfileUpdateForm
from ..form.registration import UserUpdateForm


class ProfileView:
    @method_decorator(login_required)
    def dashboard(self, request):
        return render(request, "dashboard/dashboard.html", {})

    @method_decorator(login_required)
    def blog_posts(self, request):
        return render(request, "dashboard/blog-posts.html", {})

    @method_decorator(login_required)
    def profile(self, request):
        return render(request, "dashboard/profile.html", {})

    @method_decorator(login_required)
    def update_profile(self, request):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'You account has been updated !')
                return redirect('website:profile')
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'dashboard/update-profile.html', context)

    @method_decorator(login_required)
    def comments(self, request):
        return render(request, "dashboard/comments.html", {})


