from django.db import models
from users.models import CustomUser
from football.models import FootballField


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    field = models.ForeignKey(FootballField, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.field}'
