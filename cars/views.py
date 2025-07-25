from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import BrandForm, CarForm
from .models import Brand, Car


class CarsListView(ListView):
    """
    ListView to display all cars.
    """

    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset.order_by("brand__name")


class CarsDetailView(DetailView):
    """
    DetailView to display a specific car's details.
    """

    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateCarView(CreateView):
    """
    CreateView to add a new car.
    """

    model = Car
    form_class = CarForm
    template_name = "create_car.html"
    success_url = reverse_lazy("cars_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_car_form"] = context["form"]
        return context


@method_decorator(login_required(login_url="login"), name="dispatch")
class UpdateCarView(UpdateView):
    """
    UpdateView to update a car.
    """

    model = Car
    form_class = CarForm
    template_name = "update_car.html"
    success_url = reverse_lazy("cars_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update_car_form"] = context["form"]
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})  # type: ignore


@method_decorator(login_required(login_url="login"), name="dispatch")
class DeleteCarView(DeleteView):
    """
    DeleteView to delete a car.
    """

    model = Car
    template_name = "delete_car.html"
    success_url = reverse_lazy("cars_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = self.object  # type: ignore
        return context


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateBrandView(CreateView):
    """
    CreateView to add a new car brand.
    """

    model = Brand
    form_class = BrandForm
    template_name = "create_brand.html"
    success_url = reverse_lazy("cars_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_brand_form"] = context.get("form")
        return context
