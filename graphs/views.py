import os
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from graphs.models import Stocks
from graphs.serializer import StocksSerializer


@api_view(['GET', ])
@csrf_exempt
@permission_classes([AllowAny])
def customer_get_stocks(request):
    ourstocks = StocksSerializer(
        Stocks.objects.all().order_by("-id"),
        many=True, context={"request": request}
    ).data

    return JsonResponse({"stocks": ourstocks})
