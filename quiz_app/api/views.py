from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from auth_app.api.authentication import CookieJWTAuthentication
from utils.task import create_quiz
from .serializers import QuizSerializer, UrlSerializer
from quiz_app.models import Quiz


class QuizListCreateView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        url_serializer = UrlSerializer(data=request.data)
        url_serializer.is_valid(raise_exception=True)
        video_url = url_serializer.validated_data.get("url") 
        response = create_quiz(video_url)
        quiz_data = {
            "title": response.get("title", "No Titel"),
            "description": response.get("description", ""),
            "video_url": video_url, 
            "questions": response.get("questions", [])
        }
        serializer = QuizSerializer(data=quiz_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    

    def get(self, request):
        quizzes = Quiz.objects.filter(owner=request.user)
        serializer = QuizSerializer(quizzes, many=True)
        data = serializer.data
        for quizz in data:
            for question in quizz.get("questions", []):
                question.pop("created_at")
                question.pop("updated_at")
        return Response(data=serializer.data, status=status.HTTP_200_OK)