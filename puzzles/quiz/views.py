from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Question, Category, Level, ScoreBoard
from django.contrib import messages
import json
from .forms import SignUpForm
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()  # Assuming Category is a model you've defined
        return render(request, "quiz/home.html", {"categories": categories})
    else:
        return render(request, "quiz/login.html", {})



def about(request):
    return render(request, "quiz/about.html", {})




def category(request, foo):
    foo = foo.replace("-", " ")
    return render(request, "quiz/quiz.html", {"foo": foo})


def page(request):
    questions = Question.objects.all()
    science_question = Question.objects.filter(category=9)
    return render(request, "quiz/questions.html", {"questions":questions})

def quiz(request, foo, level):
    foo = foo.replace("-", " ")
    level = level.capitalize()
    science_questions = Question.objects.filter(category__name=foo, levels__name=level).values("text", "option1", "option2", "option3", "option4", "correct_answer")
    print(science_questions)
    return render(request, "quiz/puzzles.html", {"questions": json.dumps(list(science_questions))})





def level_filter():
    levels = Level.objects.all()
    for level in levels:
        level_name = level.name
        level_id = level.id
        print(f"Category: {level_name}, ID: {level_id}")
    print(levels)
    

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


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
			# log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
            return redirect('update_info')
        else:
            messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
            return redirect('register')
    else:
        return render(request, 'quiz/register.html', {'form':form})



# Category: Geography, ID: 1
# Category: Literature, ID: 2
# Category: Science, ID: 3
# Category: Art, ID: 4
# Category: History, ID: 5
# Category: Sports, ID: 6
# Category: Movies, ID: 7
# Category: Technology, ID: 8
# Category: Music, ID: 9