from django.contrib import admin

# Register your models here.
from mfproj.mfapp.models import Peak


@admin.register(Peak)
class PoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon', 'altitude')
