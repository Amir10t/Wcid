from django.urls import path
from . import views

urlpatterns = [
    path("question/<int:id>", views.question, name="single-question"),
    path("check/<int:id>", views.check, name="check-question")
]