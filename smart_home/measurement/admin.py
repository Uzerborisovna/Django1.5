from django.contrib import admin

# Register your models here.

from .models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at']
    list_filter = ['sensor', 'created_at']