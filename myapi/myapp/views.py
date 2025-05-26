from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# vistas para la autenticacion de usuarios


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data.get('email', '')
            )
            token = Token.objects.create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProfileView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)