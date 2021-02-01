from rest_framework import serializers
from .models import Category, Subcategory, Subsubcategories, Luk


class CategoryCreateSerializer(serializers.ModelSerializer):
    """ Общий список категории """

    class Meta:
        model = Category
        fields = ('category',)


class SubcategoryCreateSerializer(serializers.ModelSerializer):
    """ Общий список категории """
    category = serializers.StringRelatedField()

    class Meta:
        model = Subcategory
        fields = ('category', 'name')


class SubsubcategoriesCreateSerializer(serializers.ModelSerializer):
    """ Общий список категории """
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Subsubcategories
        fields = ('category', 'subcategory', 'name')


class LukCreateSerializer(serializers.ModelSerializer):
    """ Общий список категории """
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    subsubcategory = serializers.StringRelatedField()

    class Meta:
        model = Luk
        fields = ('id', 'category', 'subcategory',
                  'subsubcategory', 'name', 'photo',
                  'size', 'price', 'min_price', 'percent')


class LukSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    subsubcategory = serializers.StringRelatedField()

    class Meta:
        model = Luk
        fields = ('id', 'category', 'subcategory', 'subsubcategory',
                  'name', 'photo', 'size', 'price', 'min_price', 'percent',
                  'composition', 'description', 'country',
                  'age', 'sex', 'equipment', 'season', 'appointment')

