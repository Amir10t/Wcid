from builtins import id

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import QuestionModel, QuestionCategoryModel
from random import randint

# Create your views here.
def random_question(request):
    questions = QuestionModel.objects.all()
    question = questions[randint(0,(len(questions)-1))]
    context = {
        "quiz": question,
        "not_interested_id": len(questions) + 10
    }
    return render(request, "question/single_question.html", context)
def question(request, id):
    questions = QuestionModel.objects.all()
    question=questions.get(id=id)
    context = {
        "quiz":question,
        "not_interested_id":len(questions)+10
    }
    return render(request, "question/single_question.html", context)

def check(request, id):
    questions = QuestionModel.objects.all()
    question=questions.filter(id=id).first()
    if question is None:
        new_question = questions[randint(0,(len(questions)-1))]
    else:
        new_question = find_question(question)
    url_question = reverse("single-question",args=[new_question.id])
    return redirect(url_question)

def find_question(question:QuestionModel):
    temmate = QuestionModel.objects.filter(category=question.category)
    new_question = temmate[randint(0,(len(temmate)-1))]
    while new_question == question:
        new_question = temmate[randint(0,(len(temmate)-1))]
    return new_question