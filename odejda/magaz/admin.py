from django.contrib import admin
from .models import Category, Subcategory, Subsubcategories, Luk


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'name']

    class Meta:
        verbose_name = 'Под категории'
        verbose_name_plural = 'Под категории'


@admin.register(Subsubcategories)
class SubsubcategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'subcategory', 'name']

    class Meta:
        verbose_name = 'Под подкатегории'
        verbose_name_plural = 'Под подкатегории'


@admin.register(Luk)
class LukAdmin(admin.ModelAdmin):
    search_fields = ('name', 'size', 'price', 'category', 'subcategory', 'subsubcategory')
    list_display = ('name', 'size', 'price', 'category', 'subcategory', 'subsubcategory')
    list_filter = ('size', 'name', 'price', 'category', 'subcategory', 'subsubcategory')
    fieldsets = (
        ('Category', {'fields': (('category', 'subcategory',), 'subsubcategory', 'name')}),
        ('Price', {'fields': (('price', 'percent'),)}),
        ('Size', {'fields': ('size', 'photo', 'quantity')}),
        ('Luk info', {'fields': (('description', 'composition'),
                                 'country', 'age', 'sex', 'equipment',
                                 'season', 'appointment')})

    )
    filter_horizontal = ()

    class Meta:
        verbose_name = 'Лук'
        verbose_name_plural = 'Лук'
