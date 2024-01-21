from django.urls import path
from . import views

urlpatterns = [
    path("question", views.check_user, name="question"),
    path("question/<int:id>", views.question, name="single-question"),
    path("check/<int:id>/<int:option>", views.check, name="check-question"),
    path("show-result", views.show_result, name="show-result"),
    path("delete_person_model", views.deletePersonModel, name="deletePersonModel"),
    path("test-guide", views.test_guide, name="test-guide"),
]