from django import forms
from .models import Brand
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price < 20000:
            self.add_error("price", "O preço não pode ser menor que R$ 20.000,00.")
        return price

    def clean_model_year(self):
        model_year = self.cleaned_data.get("model_year")
        if model_year and model_year < 1886:
            self.add_error("model_year", "O ano do modelo não pode ser menor que 1886.")
        return model_year

    def clean(self):
        cleaned_data = super().clean()
        model_year = cleaned_data.get("model_year")
        factory_year = cleaned_data.get("factory_year")
        if model_year and factory_year:
            if model_year > factory_year:
                self.add_error(
                    "factory_year",
                    "O ano de frabicação não pode ser maior que o ano do modelo.",
                )
        return cleaned_data


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        brand_validation = Brand.objects.filter(name__iexact=name) or None

        if brand_validation:
            self.add_error("name", "Já existe uma marca com esse nome.")
        return name
