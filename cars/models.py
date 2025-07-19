from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to="cars_images/", blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.factory_year})"


class CarInventory(models.Model):
    """
    Model of CarInventory table
    """

    id = models.AutoField(primary_key=True)
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.cars_count} {self.cars_value} ({self.created_at})"
