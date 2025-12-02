from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    """Custom JWT authentication that retrieve the token from an HTTP cookie."""


    def authenticate(self, request):
        """Authenticates the request by extracting the JWT from an HTTP cookie."""


        header = self.get_header(request)
        if header is not None:
            return super().authenticate(request)
        raw_token = request.COOKIES.get("access_token")
        if raw_token is None:
            return None
        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token