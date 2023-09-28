from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response

from .models import SpendStatistic
from .serializers import CreateSpendSerializer

# Create your views here.
class SpendView(generics.ListCreateAPIView):
    queryset = SpendStatistic.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return CreateSpendSerializer
        elif self.request.method == "POST":
            return CreateSpendSerializer

    def get(self, request, *args, **kwargs):
        
        grouped_queryset = self.queryset.values('date', 'name').annotate(
            spend=Sum('spend'),
            impressions=Sum('impressions'),
            clicks=Sum('clicks'),
            conversion=Sum('conversion'),
            revenue=Sum('revenue_statistic__revenue'),
        )
        grouped_data = list(grouped_queryset)
        
        return Response(grouped_data)
    