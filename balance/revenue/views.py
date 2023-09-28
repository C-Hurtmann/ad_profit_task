from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response

from .models import RevenueStatistic
from .serializers import RevenueSerializer

# Create your views here.
class RevenueView(generics.ListCreateAPIView):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueSerializer
    
    def get(self, request, *args, **kwargs):
        
        grouped_queryset = self.queryset.values('date', 'name').annotate(
            revenue=Sum('revenue'),
            spend_spend=Sum('spend__spend'),
            spend_impressions=Sum('spend__impressions'),
            spend_clicks=Sum('spend__clicks'),
            spend_conversion=Sum('spend__conversion')
        )
        grouped_data = list(grouped_queryset)
        return Response(grouped_data)