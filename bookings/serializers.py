from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'field', 'user', 'start_time', 'end_time']
        read_only_fields = ['user']
