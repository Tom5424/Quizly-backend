from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from auth_app.api.authentication import CookieJWTAuthentication
from utils.task import create_quiz
from .serializers import QuizSerializer


class CreateQuizView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        video_url = request.data.get("url")
        validator = URLValidator()
        try:
            validator(video_url)
        except ValidationError:
            raise DRFValidationError(detail={"url": "Invalid URL"})
        response = create_quiz(video_url)
        quiz_data = {
            "title": response.get("title", "No Titel"),
            "description": response.get("description", ""),
            "video_url": video_url, 
            "questions": response.get("questions", [])
        }
        serializer = QuizSerializer(data=quiz_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)