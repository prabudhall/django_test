from rest_framework import routers
from api.views import ItemViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='ItemsList')

urlpatterns = [
    path('', include(router.urls))
]