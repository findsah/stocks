from rest_framework import serializers
from django.db import models

from graphs.models import Stocks


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = '__all__'
