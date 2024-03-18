from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=255, verbose_name='Страна производства', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Цена без скидки(зачеркнутое)'
        )
    count = models.IntegerField(default=0, verbose_name='Количество')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

