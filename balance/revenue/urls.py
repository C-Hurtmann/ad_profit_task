from django.urls import path
from .views import RevenueView


urlpatterns = [
    path('revenues/', RevenueView.as_view(), name='revenue')
]