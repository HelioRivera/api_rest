from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    resumen = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            "description": {"required": False} # Hace que description sea opcional
        }
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
    
    def get_resumen(self, obj):
         return f"producto: {obj.name}, precio: {obj.price}"