from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Число должно быть положительным")
        return value

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Не может быть пустым.")
        return value
