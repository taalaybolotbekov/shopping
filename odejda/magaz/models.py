from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name='Категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='Categorys', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')

    def __str__(self):
        return f'{self.category}-{self.name}'

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'


class Subsubcategories(models.Model):
    category = models.ForeignKey(Category, related_name='categorylar', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategorylar', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.category}-{self.subcategory}-{self.name}'

    class Meta:
        verbose_name = 'Под подкатегории'
        verbose_name_plural = 'Под подкатегории'


class Luk(models.Model):
    name = models.CharField(max_length=400, verbose_name='Название')
    photo = models.ImageField(verbose_name='Фото одежды')
    size = models.CharField(max_length=40, verbose_name='Размеры')
    percent = models.IntegerField('Скидка в процентах', blank=True, default=0)
    price = models.IntegerField(default=0, verbose_name='Цена')
    quantity = models.IntegerField(default=0, verbose_name='Количество покупок')
    category = models.ForeignKey(Category, related_name='categorys', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategorys', on_delete=models.CASCADE)
    subsubcategory = models.ForeignKey(Subsubcategories, related_name='subsubcategory', on_delete=models.CASCADE)
    # описание
    composition = models.CharField(max_length=200, verbose_name='Состав')
    description = models.CharField(max_length=500, verbose_name='Описание')
    country = models.CharField(max_length=255, verbose_name='Страна производителя')
    age = models.CharField(max_length=255, verbose_name='Возрастная группа (лет)')
    sex = models.CharField(max_length=255, verbose_name='Пол')
    equipment = models.CharField(max_length=255, verbose_name='Комплектация')
    season = models.CharField(max_length=255, verbose_name='Сезон')
    appointment = models.CharField(max_length=300, verbose_name='Назначение')

    def __str__(self):
        return self.name

    @property
    def min_price(self):
        """Расчитать стоимость со скидкой"""
        return int(self.price * (100 - self.percent) / 100)

    class Meta:
        verbose_name = 'Лук'
        verbose_name_plural = 'Лук'

