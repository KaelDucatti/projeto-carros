from django import forms
from .models import Brand
from .models import Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200, required=True)
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all().order_by("name"),
        required=True,
        empty_label="Selecione uma marca",
    )
    factory_year = forms.IntegerField(required=False)
    model_year = forms.IntegerField(required=False)
    plate = forms.CharField(max_length=10, required=False)
    price = forms.DecimalField(max_digits=20, decimal_places=2, required=False)
    image = forms.ImageField(required=False)

    def save(self):
        car = Car(
            model=self.cleaned_data["model"],
            brand=self.cleaned_data["brand"],
            factory_year=self.cleaned_data["factory_year"],
            model_year=self.cleaned_data["model_year"],
            plate=self.cleaned_data["plate"],
            price=self.cleaned_data["price"],
            image=self.cleaned_data["image"],
        )
        car.save()
        return car


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)

    def save(self):
        brand = Brand(name=self.cleaned_data.get("name"))
        brand.save()
        return brand
