from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login-page"),
    path("logout", views.LogoutView.as_view(), name="logout-page"),
    path("user_pannel", views.UserPannelView.as_view(), name="user-pannel")
]