from django.shortcuts import render
from rest_framework import viewsets

from .models import Metric
from .serializers import MetricSerializer

# Create your views here.


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by("-time")
    serializer_class = MetricSerializer
