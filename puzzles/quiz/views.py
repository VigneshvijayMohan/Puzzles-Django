from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Question, Category
from django.contrib import messages
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()  # Assuming Category is a model you've defined
        return render(request, "quiz/home.html", {"categories": categories})
    else:
        return render(request, "quiz/login.html", {})



def about(request):
    return render(request, "quiz/about.html", {})


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



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Logged in.."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again."))
            return redirect('login')
    else: 
        return render(request, "quiz/login.html", {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out...Thanks for stopping by..."))
	return redirect('home')
