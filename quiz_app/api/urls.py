from django.urls import path
from .views import QuizListCreateView, QuizDetailView


urlpatterns = [
    path('createQuiz/', QuizListCreateView.as_view(), name="create-quiz"),
    path('quizzes/', QuizListCreateView.as_view(), name="list-quizzes"),
    path('quizzes/<int:id>/', QuizDetailView.as_view(), name="detail-quiz"),
]