from django.urls import path
from .views import upload_emissions

urlpatterns = [
    path('upload/', upload_emissions),
]