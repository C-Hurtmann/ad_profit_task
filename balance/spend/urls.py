from django.urls import path, include
from .views import SpendView


urlpatterns = [
    path('spends/', SpendView.as_view())
]