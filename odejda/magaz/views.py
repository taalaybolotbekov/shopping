from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Category, Subcategory, Subsubcategories, Luk
from .serializers import CategoryCreateSerializer, SubcategoryCreateSerializer, SubsubcategoriesCreateSerializer,\
    LukCreateSerializer, LukSerializer


class CategoryCreatApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class SubcategoryCreatApiView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryCreateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', )


class SubsubcategoriesCreatApiView(generics.ListAPIView):
    queryset = Subsubcategories.objects.all()
    serializer_class = SubsubcategoriesCreateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'subcategory')


class LukCreatApiView(generics.ListAPIView):
    queryset = Luk.objects.all()
    serializer_class = LukCreateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'subcategory', 'subsubcategory')


class LukSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Luk.objects.all()
    serializer_class = LukSerializer
