from django.contrib import admin
from .models import Profile, Category, Player, Level, Question, ScoreBoard
# Register your models here.


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Player)
admin.site.register(Level)
admin.site.register(Question)
admin.site.register(ScoreBoard)
