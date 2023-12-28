from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpRequest, HttpResponse

# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            "register_form":register_form
        }
        return render(request, "user/register.html", context)

    def post(self, request:HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_confirm_password = register_form.cleaned_data.get('confirm_password')
            match_password = str(user_password) != str(user_confirm_password)
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'Repetitious Email')
                context = {
                    "register_form": register_form
                }
                return render(request, "user/register.html", context)
            elif match_password:
                register_form.add_error('confirm_password', 'Password is not Match')
                context = {
                    "register_form": register_form
                }
                return render(request, "user/register.html", context)
            else:
                new_user = User(
                    email=user_email,
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                return HttpResponse("It\'s Done!")

        register_form = RegisterForm()
        context = {
            "register_form":register_form
        }
        return render(request, "user/register.html", context)