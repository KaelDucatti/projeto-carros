from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view, new_brand_view
from accounts.views import new_user_view, login_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", cars_view, name="cars_list"),
    path("login/", login_view, name="login"),
    path("new_car/", new_car_view, name="new_car"),
    path("new_brand/", new_brand_view, name="new_brand"),
    path("new_user/", new_user_view, name="new_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
