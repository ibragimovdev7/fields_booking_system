from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Subquery, OuterRef, F
from django.db.models.functions import JSONObject
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bookings.models import Booking
from . import filters
from .models import FootballField, FieldImage
from .permissions import IsOwnerOrReadOnly
from .serializers import FootballFieldSerializer, FieldImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class FootballFieldListView(generics.ListAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = filters.FootbalFieldFilter
    ordering_fields = ['price_per_hour']

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.annotate(
        #     broned_times=Subquery(Booking.objects.filter(field_id=OuterRef('id')), output_field=)
        # )
        queryset = queryset.annotate(
            booking_list=ArrayAgg(
                JSONObject(
                    start_time=F('bookings__start_time'),
                    end_time=F('bookings__end_time')
                )
            )
        )
        return queryset


class FootballFieldCreateView(generics.CreateAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FootballFieldRetrieveView(generics.RetrieveAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer


class FootballFieldUpdateView(generics.UpdateAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FootballFieldDestroyView(generics.DestroyAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FieldImageCreateView(generics.CreateAPIView):
    queryset = FieldImage.objects.all()
    serializer_class = FieldImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        field_id = self.kwargs['field_id']
        field = FootballField.objects.get(id=field_id)
        serializer.save(field=field)
