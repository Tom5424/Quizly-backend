from django.urls import path
from .views import QuizListCreateView


urlpatterns = [
    path('createQuiz/', QuizListCreateView.as_view(), name="create-quiz"),
    path('quizzes/', QuizListCreateView.as_view(), name="list-quizzes"),
]