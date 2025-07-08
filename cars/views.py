from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm, BrandForm


def cars_view(request):
    cars = Car.objects.all().order_by("-brand", "model")
    search = request.GET.get("search")
    if search:
        cars = cars.filter(model__icontains=search)
    return render(request, template_name="cars.html", context={"cars": cars})


def new_car_view(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
    else:
        form = CarForm()
    return render(request, template_name="new_car.html", context={"new_car_form": form})


def new_brand_view(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
    else:
        form = BrandForm()
    return render(
        request, template_name="new_brand.html", context={"new_brand_form": form}
    )
