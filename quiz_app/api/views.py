from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from auth_app.api.authentication import CookieJWTAuthentication
from utils.task import create_quiz
from .serializers import QuizSerializer, UrlSerializer


class CreateQuizView(APIView):
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