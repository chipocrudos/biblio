from django.urls.conf import include, path

app_name = 'library'

urlpatterns = [
    path('api/', include('library.api.routers'))
]
