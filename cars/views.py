from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.list import ListView

from .forms import BrandForm, CarForm
from .models import Car


class CarsListView(ListView):
    """
    ListView to display all cars.
    """

    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        queryset = super().get_queryset().order_by("brand__name")
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset


class CreateCarView(View):
    """
    View to handle the creation of a new car.
    """

    def get(self, request):
        form = CarForm()
        return render(
            request, template_name="create_car.html", context={"new_car_form": form}
        )

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
        return render(
            request, template_name="create_car.html", context={"new_car_form": form}
        )


class CreateBrandView(View):
    """
    View to handle the creation of a new car brand.
    """

    def get(self, request):
        form = BrandForm()
        return render(
            request, template_name="create_brand.html", context={"new_brand_form": form}
        )

    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
        return render(
            request, template_name="create_brand.html", context={"new_brand_form": form}
        )
