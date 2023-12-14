from django.shortcuts import render

# Create your views here.

def question(request):
    return render(request, "question/single_question.html", {})