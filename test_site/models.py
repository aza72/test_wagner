from django.db import models
from filer.fields.image import FilerImageField



class Slider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE, verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, editable=True, blank=False, null=False, verbose_name="Сортировка")

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'