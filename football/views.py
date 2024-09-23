from rest_framework import generics
from django.db.models import Q, F
from django.db.models.functions import Sqrt, Power, Cos, Radians
from rest_framework.permissions import IsAuthenticated

from .models import FootballField, FieldImage
from .permissions import IsOwnerOrReadOnly
from .serializers import FootballFieldSerializer, FieldImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class FootballFieldListView(generics.ListAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'address']
    ordering_fields = ['price_per_hour']

    def get_queryset(self):
        queryset = super().get_queryset()
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        user_lat = self.request.query_params.get('latitude')
        user_lon = self.request.query_params.get('longitude')

        if start_time and end_time:
            queryset = queryset.filter(
                ~Q(bookings__start_time__lt=end_time) &
                ~Q(bookings__end_time__gt=start_time)
            )

        if user_lat and user_lon:
            user_lat = float(user_lat)
            user_lon = float(user_lon)

            queryset = queryset.annotate(
                distance=Sqrt(
                    Power(69.1 * (F('latitude') - user_lat), 2) +
                    Power(69.1 * (user_lon - F('longitude')) * Cos(Radians(F('latitude'))), 2)
                )
            ).order_by('distance')
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