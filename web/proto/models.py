from django.db import models
from django.utils import timezone

class Prefecture(models.Model):
    name = models.CharField('都道府県名', max_length=10)
    def __str__(self):
        return self.name


class Spot(models.Model):
    name = models.CharField('観光地名', max_length=30)
    prefecture = models.ForeignKey(
        Prefecture, verbose_name='都道府県', on_delete=models.PROTECT
    )
    description = models.TextField('説明', default='')

    def __str__(self):
        return self.name
