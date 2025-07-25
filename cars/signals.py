from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from openai_api.client import get_car_ai_bio

from .models import Car, CarInventory


def car_invenroty_update():
    cars_count = Car.objects.count()
    cars_value = Car.objects.aggregate(Sum("price")).get("price__sum")
    CarInventory.objects.create(cars_count=cars_count or 0, cars_value=cars_value or 0)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invenroty_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_invenroty_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        bio = get_car_ai_bio(
            model=instance.model, brand=instance.brand, year=instance.model_year
        )
        instance.bio = bio
