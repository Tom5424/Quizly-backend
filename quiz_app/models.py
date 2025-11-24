from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField()


    def __str__(self):
       return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=200)
    question_options = models.JSONField()
    answer = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.question_title