from rest_framework import serializers

from .models import SpendStatistic


class CreateSpendSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpendStatistic
        fields = "__all__"
