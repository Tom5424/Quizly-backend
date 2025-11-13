from .views import RegisterView, CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CookieTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]