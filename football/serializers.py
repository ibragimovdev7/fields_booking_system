from rest_framework import serializers
from .models import FootballField, FieldImage


class FieldImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldImage
        fields = ['id', 'image']


class FootballFieldSerializer(serializers.ModelSerializer):
    images = FieldImageSerializer(many=True, read_only=True)

    class Meta:
        model = FootballField
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'price_per_hour', 'contact', 'images']
