from rest_framework.exceptions import ValidationError
from .models import Booking

def check_booking_availability(field, start_time, end_time):

    if Booking.objects.filter(field=field, start_time__lt=end_time, end_time__gt=start_time).exists():
        raise ValidationError("Bu vaqt oralig'ida maydon allaqachon bron qilingan.")
