from django.urls import path
from .views import SpendView


urlpatterns = [
    path('spends/', SpendView.as_view(), name='spend')
]