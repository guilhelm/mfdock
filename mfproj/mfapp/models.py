from django.db import models


class Peak(models.Model):
    name = models.CharField("Name", max_length=100)
    lat = models.DecimalField("Latitude", max_digits=7, decimal_places=5)
    lon = models.DecimalField("Longitude", max_digits=8, decimal_places=5)
    altitude = models.DecimalField("Altitude", max_digits=4, decimal_places=0)

    class Meta:
        managed = True
# Create your models here.
