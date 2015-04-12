from django.contrib import admin
from .models import Dwelling, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Dwelling)
class DwellingAdmin(admin.ModelAdmin):
    pass
