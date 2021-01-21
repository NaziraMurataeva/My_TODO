from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test")

def second(request):
    return HttpResponse("test2")

def third(request):
    return HttpResponse("this third test page")

