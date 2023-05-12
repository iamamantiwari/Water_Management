from django.urls import path
from .views import *

urlpatterns = [
    path('waterapp/',water_management_view),
]
