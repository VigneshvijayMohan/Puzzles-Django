from django.shortcuts import render

from .models import Question, Category
# Create your views here.

def home(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, "quiz/home.html", {"categories":categories})


# def category(request, foo):
#     foo = foo.replace("-", " ")
#     question = Question.objects.filter(category__name=foo)
#     print(question)
#     return render(request, "quiz/quiz.html", {})


def category(request, foo):
    foo = foo.replace("-", " ")
    return render(request, "quiz/quiz.html", {"foo": foo})


def page(request):
    questions = Question.objects.all()
    return render(request, "quiz/questions.html", {"questions":questions})