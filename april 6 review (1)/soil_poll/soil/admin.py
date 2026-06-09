from django.contrib import admin
from .models import Crop

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'emoji', 'min_ph', 'max_ph', 'min_moisture', 'max_moisture', 'min_temperature', 'max_temperature', 'priority')
    list_filter = ('priority', 'created_at')
    search_fields = ('name', 'description')
    ordering = ['-priority']
