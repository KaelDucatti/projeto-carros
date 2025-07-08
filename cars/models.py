from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to="cars_images/", blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.factory_year})"
