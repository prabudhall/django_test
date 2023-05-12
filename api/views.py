from django.shortcuts import render

from rest_framework import viewsets
from api.models import ItemsList
from api.serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemsList.objects.all()
    serializer_class = ItemSerializer
