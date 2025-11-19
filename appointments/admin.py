from django.contrib import admin
from .models import Schedule, Appointment  # importar ambos modelos

admin.site.register(Schedule)
admin.site.register(Appointment)
