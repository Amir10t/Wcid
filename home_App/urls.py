from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("test", views.test)

]