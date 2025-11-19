from django.contrib import admin
from .models import PQRS  # asegúrate que coincida con el nombre de la clase

@admin.register(PQRS)
class PQRSAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "type", "subject", "status", "created_at")
    list_filter = ("status", "type", "created_at")
    search_fields = ("subject", "description", "patient__name")
