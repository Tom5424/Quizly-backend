from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.contrib.auth.models import User
# from .authentication import CookieJWTAuthentication
# from .serializers import CreateQuizSerializer
from utils.task import create_quiz
 

class CreateQuizView(APIView):


    def post(self, request):
        url = request.data.get("url")
        response = create_quiz(url)
        return Response(data=response, status=status.HTTP_201_CREATED)