from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test")

def second(request):
    return render(request, "second.html")

def third(request):
    return render(request, "third.html")

