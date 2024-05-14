from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =models.CharField(max_length=20, blank=True)
    
    
    def __str__(self):
        return self.user.username
    

class Description(models.Model): 
    description= models.CharField(max_length=200)
    def __str__(self):
        return self.description
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description= models.CharField(max_length=200 , default = 0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    points = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    levels = models.ManyToManyField(Level)
    text = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')])
    # explanation = models.TextField(blank=True)  # Optional explanation for the correct answer
    # image = models.ImageField(upload_to='question_images/', blank=True)  # Optional image for the question

    # Additional fields for flexibility and customization
    # question_type = models.CharField(max_length=20, default='Multiple Choice')  # Type of question
    # difficulty_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)  # Difficulty level

    def __str__(self):
        return self.text[:50]  # Display first 50 characters of the question text



from django.db import models
from django.contrib.auth.models import User

class ScoreBoard(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category  = models.CharField(max_length=50, default = 0)
    level =  models.CharField(max_length=50, default=0)
    

    def __str__(self):
        return f"Percentage of {self.player.username}: {self.percentage}%"


