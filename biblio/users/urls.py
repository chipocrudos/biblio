from django.urls import include, path

app_name = "users"

urlpatterns = [path("api/", include("users.api.routers"))]
