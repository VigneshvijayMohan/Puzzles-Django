from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Question, Category, Level, ScoreBoard
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        categories = Category.objects.all() 
        return render(request, "quiz/home.html", {"categories": categories})
    else:
        return render(request, "quiz/login.html", {})



def about(request):
    categories = Category.objects.all()
    return render(request, "quiz/about.html", {"categories": categories})




def category(request, foo):
    foo = foo.replace("-", " ")
    categories = Category.objects.all()
    return render(request, "quiz/quiz.html", {"foo": foo, "categories": categories})


def page(request):
    questions = Question.objects.all()
    science_question = Question.objects.filter(category=9)
    return render(request, "quiz/questions.html", {"questions":questions})


@login_required
def quiz(request, foo, level):
    foo = foo.replace("-", " ")
    level = level.capitalize()
    science_questions = Question.objects.filter(category__name=foo, levels__name=level).values("text", "option1", "option2", "option3", "option4", "correct_answer")

    if request.method == 'POST':
        player = request.user
        total_questions = len(science_questions)
        correct_answers = int(request.POST.get('score'))  # Assuming score is the number of correct answers
        percentage = (correct_answers / total_questions) * 100
        category = foo
        level = level
        ScoreBoard.objects.create(player=player, percentage=percentage, category = category, level = level)
        messages.success(request, 'Your percentage has been saved successfully!')
        return redirect(reverse('home'))  # Redirect to home page after saving percentage

    
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

def score(request):
    if request.user.is_authenticated:
        categories = Category.objects.all() 
        scores = ScoreBoard.objects.all().order_by('-percentage') # Assuming Category is a model you've defined
        context = {
        'scores': scores,
        "categories": categories,
    }
        return render(request, "quiz/scorecard.html", context)
    else:
        return render(request, "quiz/login.html", {})

# Category: Geography, ID: 1
# Category: Literature, ID: 2
# Category: Science, ID: 3
# Category: Art, ID: 4
# Category: History, ID: 5
# Category: Sports, ID: 6
# Category: Movies, ID: 7
# Category: Technology, ID: 8
# Category: Music, ID: 9