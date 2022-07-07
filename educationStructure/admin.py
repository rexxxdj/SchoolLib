from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ['id', 'name']
    ordering = ['id', 'name']
    list_per_page = 10
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', )
    list_display_links = ['id', 'name']
    list_editable = ['country']
    ordering = ['id', 'country', 'name']
    list_filter = ['country']
    list_per_page = 10
    search_fields = ['name']


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'city', 'notes']
    list_display_links = ['id', 'name']
    list_editable = ['country', 'city']
    ordering = ['id', 'country', 'city', 'name']
    list_filter = ['country', 'city']
    list_per_page = 10
    search_fields = ['name', 'notes']


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Institution, InstitutionAdmin)


# Register your models here.

'''


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Institution, InstitutionAdmin)
'''
