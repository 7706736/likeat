from django.urls import path
from pagprincipal.views import inicio


urlpatterns = [
    path('', inicio, name="index"),
]
