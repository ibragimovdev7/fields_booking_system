import django_filters
from django.db.models import Q, F
from django.db.models.functions import Sqrt, Power, Cos, Radians
from django.utils.dateparse import parse_datetime

from football.models import FootballField


class FootbalFieldFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    time = django_filters.CharFilter(label='2024-09-23T00:00:00,2024-09-25T23:59:59', method='time_filter')
    user_location = django_filters.CharFilter(label='"lon,lat,radius(km)" - ex: "44.005,45.60,10"',
                                              method='distance_filter')

    class Meta:
        model = FootballField
        fields = ['name', 'address', 'time']

    def time_filter(self, queryset, name, value):
        start_datetime_str, end_datetime_str = value.split(',')
        start_time = parse_datetime(start_datetime_str)
        end_time = parse_datetime(end_datetime_str)
        if start_time and end_time:
            queryset = queryset.filter(
                ~Q(bookings__start_time__lt=end_time) &
                ~Q(bookings__end_time__gt=start_time)
            )
        return queryset

    def distance_filter(self, queryset, name, value):
        user_lat, user_lon, radius = value.split(',')
        if user_lat and user_lon and radius:
            user_lat = float(user_lat)
            user_lon = float(user_lon)
            radius = float(radius)

            queryset = queryset.annotate(
                distance=Sqrt(
                    Power(69.1 * (F('latitude') - user_lat), 2) +
                    Power(69.1 * (user_lon - F('longitude')) * Cos(Radians(F('latitude'))), 2)
                )
            ).filter(distance__lte=radius).order_by('distance')
        return queryset
