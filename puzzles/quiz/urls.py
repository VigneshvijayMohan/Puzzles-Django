from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('quiz/<str:foo>/', views.category, name='category'),
    path("page/", views.page, name="page"),
]