from django.contrib import admin
from .models import Country_total_deaths


class Country_total_deaths_Admin(admin.ModelAdmin):
    list_display = ('id','country','deaths')



# Register your models here.
admin.site.register(Country_total_deaths,Country_total_deaths_Admin)