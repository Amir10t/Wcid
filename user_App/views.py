import msvcrt

from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .models import PersonModel
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, EditFullnameForm
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
                    is_active=True,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse("login-page"))

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
                    return redirect(reverse('question'))
                else:
                    login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'user/login.html', context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('question'))

class UserPannelView(View):
    def get(self, request: HttpRequest):
        if request.user.id != None:
            user: User = User.objects.filter(email__iexact=request.user.email).first()
            person_model: PersonModel = PersonModel.objects.filter(user_id__exact=request.user.id).first()
            context = {
                "user":user,
                "person_model":person_model
            }
            return render(request, "user/user_pannel.html", context)
        else:
            login_form = RegisterForm()
            context = {
                "login_form": login_form
            }
            return render(request, "user/login.html", context)


class EditFullnameView(View):
    def get(self, request: HttpRequest):
        if request.user.id != None:
            edit_fullname_form = EditFullnameForm()
            context = {
                "edit_fullname_form": edit_fullname_form
            }
            return render(request, "user/editFullname.html", context)
        else:
            login_form = RegisterForm()
            context = {
                "login_form": login_form
            }
            return render(request, "user/login.html", context)
    def post(self, request: HttpRequest):
        edit_fullname_form = EditFullnameForm(request.POST)
        if edit_fullname_form.is_valid():
            user: User = User.objects.filter(email__iexact=request.user.email).first()
            first_name = edit_fullname_form.cleaned_data.get('first_name')
            last_name = edit_fullname_form.cleaned_data.get('last_name')
            user.first_name = first_name
            user.last_name  = last_name
            user.save()

            return redirect(reverse("user-pannel"))

        edit_fullname_form = EditFullnameForm()
        context = {
            "edit_fullname_form": edit_fullname_form
        }
        return render(request, "user/editFullname.html", context)