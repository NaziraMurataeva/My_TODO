from django.shortcuts import render, HttpResponse,redirect
from .models import ToDo, Books


def homepage(request):
    return render(request, "fourth.html")

def test(request):
    return render(request, "test.html")

def second(request):
    todo_list = ToDo.objects.all()
    return render(request, "second.html",{"todo_list": todo_list} )

def third(request):
    
    return render(request, "third.html", )

def somepage(request):
    return render(request, "index.html")

def books(request):
    books = Books.objects.all()
    return render(request, "books.html", {"books": books} )

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(second)

def add_book(request):
    form = request.POST
    book = Books (
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        genre=form["genre"],
        author=form["author"],
        year= form["year"],
        date=form["date"][:10],
        price=form["price"],
    )
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(second)

def delete_book(request, id):
    b = Books.objects.get(id=id)
    b.delete()
    return redirect(books)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(second)


def details(request, id):
    books_object = Books.objects.get(id=id)
    return render(request, "books_detail.html", {"books_object": books_object} )

def close_todo(request, id):
    todo =ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(second)

def f_book(request, id):
    book = Books.objects.get(id=id)
    book.is_fav = not book.is_fav
    book.save()
    return redirect(books)

def book(request):
    return render(request, "books.html", )



