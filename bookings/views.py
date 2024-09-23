from rest_framework import generics
from .models import Booking, FootballField
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from football.permissions import IsOwner
from rest_framework.exceptions import ValidationError
from .helpers import check_booking_availability
from django.db import transaction


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        field_id = self.request.data.get('field')
        start_time = self.request.data.get('start_time')
        end_time = self.request.data.get('end_time')

        try:
            field = FootballField.objects.get(id=field_id)
        except FootballField.DoesNotExist:
            raise ValidationError("Maydon topilmadi.")

        check_booking_availability(field, start_time, end_time)

        serializer.save(user=self.request.user, field=field)


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDestroyView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
