from django.contrib import admin
from cars.models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "model",
        "brand",
        "factory_year", 
        "model_year",
        "price"
    )
    search_fields = ("model", "brand", "factory_year", "model_year")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
