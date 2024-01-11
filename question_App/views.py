from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import QuestionModel, QuestionCategoryModel
from user_App.models import PersonModel
from random import randint

# مقادیر
turn = 0
clicked = []
correct_clicked = []

def random_question(request):
    global turn, clicked, correct_clicked
    turn = 0
    clicked, correct_clicked = [], []
    questions = QuestionModel.objects.all()
    question = questions[randint(0,(len(questions)-1))]
    context = {
        "quiz": question,
        "show":False
    }
    return render(request, "question/single_question.html", context)

def question(request, id):
    global turn
    questions = QuestionModel.objects.all()
    question=questions.get(id=id)
    context = {
        "quiz":question,
        "show": True if turn >= 5 else False
    }
    return render(request, "question/single_question.html", context)

def check(request, id, option):
    global turn
    questions = QuestionModel.objects.all()
    question=questions.filter(id=id).first()
    if option == int(question.correct_answer):
        turn += 1
        clicked.append(question.category)
        correct_clicked.append(question.category)
        return HttpResponse(f"{clicked} ----- {correct_clicked}")
    elif option == 5:
        new_question = questions[randint(0,(len(questions)-1))]
        while new_question.category == question.category:
            new_question = questions[randint(0, (len(questions) - 1))]
    else:
        turn += 1
        clicked.append(question.category)
        new_question = find_question(question)
    url_question = reverse("single-question",args=[new_question.id])
    return redirect(url_question)

def show_result(request):
    if clicked == []: # جلوگیری از ارور
        favorite = "نامعلوم"
    else:
        favorite = most_frequent(clicked)
    if correct_clicked == []: # جلوگیری از ارور
        ability = "نامعلوم"
    else:
        ability = most_frequent(correct_clicked)
    context = {
        "ability":ability,
        "favorite":favorite,
        "len_question":len(clicked)
    }
    new_personModel = PersonModel(
        user=request.user,
        ability=ability,
        favorite=favorite
    )
    new_personModel.save()
    return render(request, "question/result.html", context)


#  -------------- TOOLS :

def find_question(question:QuestionModel): # یک سوال بهش میدی و یک سوال دیگه بهت از همون شاخه میده
    temmate = QuestionModel.objects.filter(category=question.category)
    new_question = temmate[randint(0,(len(temmate)-1))]
    while new_question == question:
        new_question = temmate[randint(0,(len(temmate)-1))]
    return new_question


def most_frequent(List:list): # پیدا کردن عضوی بیشتر در مجموعه تکرار شده
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num