from django.urls import path

from .views import *

urlpatterns = [
    path('', HelloRekruto.as_view()),
]
