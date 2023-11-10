from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


class OmborModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ombor.objects.all()
    serializer_class = OmborSerializer

class MaxsulotModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Maxsulot.objects.all()
    serializer_class = OmborSerializer

class MijozModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

class StatistikaModelViewSet(ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaSerializer