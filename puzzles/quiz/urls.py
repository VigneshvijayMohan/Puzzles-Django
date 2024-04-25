from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('quiz/<str:foo>/', views.category, name='category'),
    path("page/", views.page, name="page"),
    path("login/",views.login_user, name = "login" ),
    path("logout/",views.logout_user, name = "logout" ),
    
]