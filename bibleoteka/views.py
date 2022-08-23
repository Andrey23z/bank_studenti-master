from django.shortcuts import render
from .utils import DataMixin, menu
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import *



class BookHome(DataMixin, ListView):
    model = Book
    template_name = 'Book/index.html'
    context_object_name = 'posts'

menu = ["О сайте", "Добавить статью", " Обратная связь", "Войти"]

# получение данных из бд
def index(request):
    posts = Book.objects.all()
    return render(request, 'Book/index.html', {'menu': menu, 'posts': posts, 'title': 'Главная страница'})

def about(request):
    return render(request, 'Book/about.html', {'menu': menu, 'title': 'О сайте'})





# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Book()
        tom.name = request.POST.get("name")
        tom.genre = request.POST.get("genre")
        tom.save()
    return HttpResponseRedirect("/")


def views():
    return None


# изменение данных в бд
def edit(request, id):
    try:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            book.name = request.POST.get("name")
            book.genre = request.POST.get("genre")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")