from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('quiz/<str:foo>/', views.category, name='category'),
    path('quiz/<str:foo>/<str:level>/', views.quiz, name='quiz'),
    path("page/", views.page, name="page"),
    path("login/",views.login_user, name = "login" ),
    path("logout/",views.logout_user, name = "logout" ),
    path("register/",views.register_user, name = "register" ),
    path("score/", views.score, name="score"),
    
]