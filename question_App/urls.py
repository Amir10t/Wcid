from django.urls import path
from . import views

urlpatterns = [
    path("", views.question, name="single-question")
]