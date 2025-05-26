from rest_framework import serializers
from .models import Product
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):

    # resumen = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['id', 'name', 'price', 'description', 'resumen']
        # fields = ['id', 'name', 'price']
        # extra_kwargs = {
        #     "description": {"required": False} # Hace que description sea opcional
        # }
    
    # def validate_price(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Price must be a positive number.")
    #     return value
    
    # def get_resumen(self, obj):
    #      return f"producto: {obj.name}, precio: {obj.price}"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")