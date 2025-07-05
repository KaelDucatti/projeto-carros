from django.shortcuts import render
from .models import Car


def cars_view(request):
    cars = Car.objects.all().order_by("-brand", "model")

    search = request.GET.get("search")
    if search:
        cars = cars.filter(model__icontains=search)


    return render(
        request, 
        template_name="cars.html", 
        context={"cars": cars}
    )   
