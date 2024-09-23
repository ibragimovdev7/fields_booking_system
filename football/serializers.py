from datetime import datetime, timedelta

from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from rest_framework import serializers
from .models import FootballField, FieldImage


class FieldImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldImage
        fields = ['id', 'image']


class FootballFieldSerializer(serializers.ModelSerializer):
    images = FieldImageSerializer(many=True, read_only=True)
    distance = serializers.FloatField(allow_null=True, read_only=True)
    free_times = serializers.SerializerMethodField(method_name='get_free_times')

    class Meta:
        model = FootballField
        fields = ['id', 'name', 'address', 'latitude',
                  'longitude', 'price_per_hour', 'contact',
                  'images', 'distance', 'free_times']

    def get_free_times(self, instance):
        start_time = make_aware(datetime.now())
        end_time = make_aware(datetime.now() + timedelta(days=7))
        free_slots = []

        booked_times = sorted(instance.booking_list, key=lambda x: x['start_time']) if instance.booking_list else []
        current_time = start_time

        for booking in booked_times:
            t1 = parse_datetime(booking['start_time'])
            t2 = parse_datetime(booking['end_time'])
            if current_time < t1:
                free_slots.append({
                    'start_time': current_time,
                    'end_time': t1
                })
            current_time = max(current_time, t2)

        if current_time < end_time:
            free_slots.append({
                'start_time': current_time,
                'end_time': end_time
            })
        return free_slots
