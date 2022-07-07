from django.db import models
from django.urls import reverse


class Country(models.Model):
    class Meta(object):
        verbose_name = u"Країна"
        verbose_name_plural = u"Країни"
        ordering = ['name']

    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name=u"Назва країни")

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta(object):
        verbose_name = u"Місто"
        verbose_name_plural = u"Міста"

    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name=u"Назва")
    country = models.ForeignKey(
        Country,
        db_index=True,
        on_delete=models.PROTECT,
        verbose_name=u"Країна")

    def __str__(self):
        return self.name


class Institution(models.Model):
    class Meta(object):
        verbose_name = u"Учбовий заклад"
        verbose_name_plural = u"Учбові заклади"

    name = models.CharField(
        max_length=1024,
        db_index=True,
        verbose_name=u"Назва")
    country = models.ForeignKey(
        Country,
        db_index=True,
        on_delete=models.PROTECT,
        verbose_name=u"Країна")
    city = models.ForeignKey(
        City,
        db_index=True,
        on_delete=models.PROTECT,
        verbose_name=u"Місто")
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __str__(self):
        return self.name
