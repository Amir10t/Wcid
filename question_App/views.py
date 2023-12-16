from django.http import HttpResponse
from django.shortcuts import render
from .models import QuestionModel, QuestionCategoryModel
from random import randint

# Create your views here.

def question(request, id):
    questions = QuestionModel.objects.all()
    question=questions.get(id=id)
    return render(request, "question/single_question.html", {"quiz":question})

def check(request, id):
    questions = QuestionModel.objects.all()
    question=questions.get(id=id)
    temmate = QuestionCategoryModel.objects.filter(question_category=question.category)
    new_question = temmate[randint(0,(len(temmate)-1))]
    return HttpResponse(new_question)