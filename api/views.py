from django.shortcuts import render

from rest_framework import viewsets
from api.models import ItemsList
from api.serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):

    serializer_class = ItemSerializer
    # queryset = ItemsList.objects.all()
    def get_queryset(self):
        queryset = ItemsList.objects.all()
        # print(self.request.GET.keys())
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        subcategory = self.request.query_params.get('subcategory', None)
        amount = self.request.query_params.get('amount', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        elif category is not None:
            queryset = queryset.filter(category=category)
        elif subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)
        elif amount is not None:
            queryset = queryset.filter(amount=amount)
        return queryset
