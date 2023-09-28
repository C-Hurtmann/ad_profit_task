from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import SpendStatistic
from revenue.models import RevenueStatistic
# Create your tests here.

class SpendViewTestCase(TestCase):
    
    url = reverse('spend')
    
    def setUp(self):
        spend_1 = SpendStatistic.objects.create(name='Test1', date='2023-09-28', spend=50, impressions=1, clicks=2, conversion=1)
        spend_2 = SpendStatistic.objects.create(name='Test1', date='2023-09-28', spend=48, impressions=1, clicks=7, conversion=2)
        spend_3 = SpendStatistic.objects.create(name='Test2', date='2023-09-29', spend=49, impressions=1, clicks=4, conversion=1)
        revenue = RevenueStatistic.objects.create(name='TestRevenue', date='2023-09-28', revenue=20.99, spend=spend_3)
    
    def tearDown(self):
        SpendStatistic.objects.delete()
        RevenueStatistic.objects.delete()
    
    def test_get_statistic(self):
        response = self.client.get(self.url)
        obj_1 = response.data[0]
        obj_2 = response.data[1]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test first object
        self.assertEqual(obj_1['spend'], 98)
        self.assertEqual(obj_1['impressions'], 2)
        self.assertEqual(obj_1['clicks'], 9)
        self.assertEqual(obj_1['conversion'], 3)
        self.assertIsNone(obj_1['revenue'])
        # test second object
        self.assertEqual(obj_2['spend'], 49)
        self.assertEqual(obj_2['impressions'], 1)
        self.assertEqual(obj_2['clicks'], 4)
        self.assertEqual(obj_2['conversion'], 1)
        self.assertEqual(obj_2['revenue'], Decimal('20.99'))
        
