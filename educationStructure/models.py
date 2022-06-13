from django.db import models

class Country(models.Model):
    class Meta(object):
        verbose_name = u"Країна"
        verbose_name_plural = u"Країни"

    name = models.CharField(
        max_length=50,
        verbose_name=u"Назва країни")

class City(models.Model):
    class Meta(object):
        verbose_name = u"Місто"
        verbose_name_plural = u"Міста"

    name = models.CharField(
        max_length=50,
        verbose_name=u"Назва")
    countryId = models.ForeignKey(
        Country,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=u"Країна")

class Institution(models.Model):
    class Meta(object):
        verbose_name = u"Учбовий заклад"
        verbose_name_plural = u"Учбові заклади"

    name = models.CharField(
        max_length=1024,
        verbose_name=u"Назва")
    countryId = models.ForeignKey(
        Country,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=u"Країна")
    cityId = models.ForeignKey(
        City,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=u"Місто")
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")
