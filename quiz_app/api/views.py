from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from auth_app.api.authentication import CookieJWTAuthentication
from utils.task import create_quiz
from .serializers import QuizSerializer, UrlSerializer
from .permissions import IsOwner
from quiz_app.models import Quiz


class QuizListCreateView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        url_serializer = UrlSerializer(data=request.data)
        url_serializer.is_valid(raise_exception=True)
        video_url = url_serializer.validated_data.get("url") 
        response = create_quiz(video_url)
        if response is None:
            return Response(data={"error": "The video is too long. Only Videos with a duration of 5 minutes allowed."}, status=status.HTTP_400_BAD_REQUEST)
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


class QuizDetailView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]


    def get(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        self.check_object_permissions(request, quiz)
        serializer = QuizSerializer(quiz)
        data = serializer.data
        for question in data.get("questions", []):
                question.pop("created_at")
                question.pop("updated_at")
        return Response(data=data, status=status.HTTP_200_OK)
    

    def patch(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        self.check_object_permissions(request, quiz)
        serializer = QuizSerializer(quiz, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        data = serializer.data
        for question in data.get("questions", []):
                question.pop("created_at")
                question.pop("updated_at")
        return Response(data=data, status=status.HTTP_200_OK)
    

    def delete(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        self.check_object_permissions(request, quiz)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)