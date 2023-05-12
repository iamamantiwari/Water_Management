from django.contrib import admin
from .models import WaterManagement


@admin.register(WaterManagement)
class WaterManagementAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_water_consumed', 'total_cost')

