from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html",)

def test(request):
    return render(request, "test.html")

def second(request):
    todo_list = ToDo.objects.all()
    return render(request, "second.html", {"todo_list": todo_list})

def third(request):
    return render(request, "third.html")

def somepage(request):
    return render(request, "fourth.html")

