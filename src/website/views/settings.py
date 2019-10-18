from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

from ..form.settings import ChangeEmailAddress, ChangeUsername


class ProfileSetting:

    @method_decorator(login_required)
    def settings(self, request):
        change_pass_form = PasswordChangeForm(request.user)
        return render(request, "dashboard/settings.html", {
            'change_pass_form': change_pass_form
        })

    @method_decorator(login_required)
    def change_username(self, request):
        return 0

    @method_decorator(login_required)
    def change_email(self, request):
        return 0
