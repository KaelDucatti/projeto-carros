from django.contrib import admin

from cars.models import Brand, Car, CarInvertory


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "brand", "factory_year", "model_year", "price")
    search_fields = ("model", "brand", "factory_year", "model_year")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(CarInvertory)
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "cars_count", "cars_value", "created_at")
    search_fields = ("cars_count", "cars_value", "crated_at")
    list_filter = ("created_at",)
    date_hierachy = "created_at"
