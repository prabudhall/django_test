from django.contrib import admin
from api.models import ItemsList

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount')


# Register your models here.
admin.site.register(ItemsList, ItemAdmin)

# python manage.py createsuperadmin

