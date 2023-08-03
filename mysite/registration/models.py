from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.geoip2 import GeoIP2


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    device_name = models.CharField(max_length=100)
    login_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # При сохранении объекта, автоматически определить геолокацию по IP-адресу
        g = GeoIP2()
        city_data = g.city(self.ip_address)
        self.location = Point(city_data['longitude'], city_data['latitude'])
        super().save(*args, **kwargs)
