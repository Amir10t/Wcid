from django.shortcuts import render
from .models import QuestionModel

# Create your views here.

def question(request, id):
    questions = QuestionModel.objects.all()
    question=questions.get(id=id)
    return render(request, "question/single_question.html", {"quiz":question})