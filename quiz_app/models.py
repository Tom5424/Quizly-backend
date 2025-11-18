from django.db import models
from utils import answer_choices


class Quiz(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField()


    def __str__(self):
       return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=100)
    question_options = models.CharField(max_length=25, choices=answer_choices)
    answer = models.CharField(max_length=25) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.question_title