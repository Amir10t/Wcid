from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
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
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
                context = {
                    "register_form": register_form
                }
                return render(request, "user/register.html", context)
            elif match_password:
                register_form.add_error('confirm_password', 'گذرواژه با تکرارش مطابقت ندارد')
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

class LoginView(View):
    def get(self, request):
        login_form = RegisterForm()
        context = {
            "login_form":login_form
        }
        return render(request, "user/login.html", context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                is_password_correct = user.check_password(user_password)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home_page'))
                else:
                    login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'user/login.html', context)