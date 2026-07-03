from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import User
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer
)

class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=201
            )

        return Response(serializer.errors, status=400)
    
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:

                return Response(
                    {
                        "error": "Invalid email or password"
                    },
                    status=400
                )

            user = authenticate(
                username=user.username,
                password=password
            )

            if user:

                return Response({

                    "message": "Login Successful",

                    "role": user.role,

                    "username": user.username,

                    "email": user.email

                })

            return Response(

                {
                    "error": "Invalid email or password"
                },

                status=400

            )

        return Response(serializer.errors, status=400)

class UserListView(APIView):

    def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    