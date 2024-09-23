from rest_framework import serializers
from .models import FootballField, FieldImage


class FieldImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldImage
        fields = ['id', 'image']


class FootballFieldSerializer(serializers.ModelSerializer):
    images = FieldImageSerializer(many=True, read_only=True)
    distance = serializers.FloatField(allow_null=True, read_only=True)
    broned_times = serializers.SerializerMethodField(method_name='get_broned_times')

    class Meta:
        model = FootballField
        fields = ['id', 'name', 'address', 'latitude',
                  'longitude', 'price_per_hour', 'contact',
                  'images', 'distance', 'broned_times']

    def get_broned_times(self, instance):
        print('------', instance)
        return 'x'
