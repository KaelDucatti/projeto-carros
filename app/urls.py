from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import CreateUserView, LoginView, LogoutView
from cars.views import (
    CarsDetailView,
    CarsListView,
    CreateBrandView,
    CreateCarView,
    DeleteCarView,
    UpdateCarView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("car/create/", CreateCarView.as_view(), name="create_car"),
    path("car/<int:pk>/", CarsDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", UpdateCarView.as_view(), name="car_update"),
    path("car/<int:pk>/delete/", DeleteCarView.as_view(), name="car_delete"),
    path("brand/create", CreateBrandView.as_view(), name="create_brand"),
    path("user/create", CreateUserView.as_view(), name="create_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
