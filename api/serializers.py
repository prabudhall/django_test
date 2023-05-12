from rest_framework import serializers
from api.models import ItemsList

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # items_id = serializers.ReadOnlyField()     # to show the id also while displaying the complete data. But we can only read this field and cannot update this field
    class Meta:
        model = ItemsList
        fields = ['name', 'category', 'subcategory', 'amount']      #"__all__"      # it can be a list of required fields ['name', 'amount']
