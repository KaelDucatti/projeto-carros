from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import CreateUserView, LoginView, LogoutView
from cars.views import CarsDetailView, CarsListView, CreateBrandView, CreateCarView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CarsListView.as_view(), name="cars_list"),
    path("car/<int:pk>/", CarsDetailView.as_view(), name="cars_detail"),
    path("create_brand/", CreateBrandView.as_view(), name="create_brand"),
    path("create_car/", CreateCarView.as_view(), name="create_car"),
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
