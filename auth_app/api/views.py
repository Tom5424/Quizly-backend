from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserInfoSerializer


class RegisterView(APIView):


    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"detail": "User created successfully!"}, status=status.HTTP_201_CREATED)
    

class CookieTokenObtainPairView(TokenObtainPairView):


    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access = response.data.get("access")
        refresh = response.data.get("refresh")
        username = request.data.get("username")
        user = User.objects.filter(username=username).first()
        response.set_cookie(key="access_token", value=access, httponly=True, secure=True, samesite="Lax")
        response.set_cookie(key="refresh_token", value=refresh, httponly=True, secure=True, samesite="Lax")
        response.data = {"detail": "Login successfully!", "user": UserInfoSerializer(user).data}
        return response