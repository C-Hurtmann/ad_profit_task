from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import RevenueStatistic
from spend.models import SpendStatistic
# Create your tests here.

class RevenueViewTestCase(TestCase):
    url = reverse('revenue')
    
    def setUp(self):
        spend_1 = SpendStatistic.objects.create(name='TestSpend1', date='2023-09-28', spend=50, impressions=1, clicks=2, conversion=1)
        spend_2 = SpendStatistic.objects.create(name='TestSpend2', date='2023-09-28', spend=33.99, impressions=2, clicks=2, conversion=1)
        revenue_1 = RevenueStatistic.objects.create(name='Test1', date='2023-09-28', revenue=20.99, spend=spend_1)
        revenue_2 = RevenueStatistic.objects.create(name='Test1', date='2023-09-28', revenue=10, spend=spend_2)
        revenue_3 = RevenueStatistic.objects.create(name='Test2', date='2023-09-28', revenue=55.35, spend=spend_2)
        
    def tearDown(self):
        SpendStatistic.objects.all().delete()
        RevenueStatistic.objects.all().delete()
    
    def test_get_statistic(self):
        response = self.client.get(self.url)
        obj_1 = response.data[0]
        obj_2 = response.data[1]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test first object
        self.assertEqual(obj_1['revenue'], Decimal('30.99'))
        self.assertEqual(obj_1['spend_spend'], Decimal('83.99'))
        self.assertEqual(obj_1['spend_impressions'], 3)
        self.assertEqual(obj_1['spend_clicks'], 4)
        self.assertEqual(obj_1['spend_conversion'], 2)
        # test second object
        self.assertEqual(obj_2['revenue'], Decimal('55.35'))
        self.assertEqual(obj_2['spend_spend'], Decimal('33.99'))
        self.assertEqual(obj_2['spend_impressions'], 2)
        self.assertEqual(obj_2['spend_clicks'], 2)
        self.assertEqual(obj_2['spend_conversion'], 1)