from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from api.models import ItemsList
from api.serializers import ItemSerializer
from django.http import JsonResponse
from django.urls.exceptions import NoReverseMatch
# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):

    serializer_class = ItemSerializer
    queryset = ItemsList.objects.all()
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'put', 'delete']
    def list(self, request, *args, **kwargs):
        queryset = ItemsList.objects.all()
        # print(self.request.GET.keys())
        if self.request.method == 'GET':
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
        else:
            return JsonResponse({'error': 'cannot see in other method than GET'})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if len(request.query_params) > 0 and request.method != 'GET':
            raise ValidationError({'error': 'cannot see in other method than GET'})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        try:
            if len(request.query_params) > 0 and request.method != 'GET':
                raise ValidationError({'error': 'cannot see in other method than GET'})

            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except ValidationError as e:
            print('\n\n\n\n\n\n')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('\n\n\n\n\n\n')
            if 'APPEND_SLASH' in e:
                return Response({'error': 'Please include a trailing slash in the URL.'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'unexpected'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if len(request.query_params) > 0 and request.method != 'GET':
            raise ValidationError({'error': 'cannot see in other method than GET'})

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'delete': f'deleted {kwargs["pk"]} successfully'}, status=status.HTTP_204_NO_CONTENT)

# in the new version it is required to write the queryset in the begin. if you need to do the changes then in the urls.py
# where you are setting the url there you have to add the parameter basename='model_name'
# eg. - router = routers.DefaultRouter()
# router.register(r'items', ItemViewSet, basename='ItemsList')