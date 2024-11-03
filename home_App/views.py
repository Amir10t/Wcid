from django.shortcuts import render
from django.views.generic import View
from .models import TestModel
from random import randint

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html", {})

def test(request):
    radnom_number = randint(1, 4)
    data = TestModel.objects.filter(id=radnom_number).first()
    context = {
        "data": data
    }

    return  render(request, "home/test.html", context)