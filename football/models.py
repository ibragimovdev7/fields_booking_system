from django.db import models
from users.models import CustomUser

class FootballField(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class FieldImage(models.Model):
    field = models.ForeignKey(FootballField, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='field_images/')

    def __str__(self):
        return f"Image for {self.field.name}"