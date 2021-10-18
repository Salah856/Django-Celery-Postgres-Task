from django.urls import path
from .views import alphaVantageAPI


urlpatterns = [
    path('/quotes', alphaVantageAPI),
]
