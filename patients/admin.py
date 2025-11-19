from django.contrib import admin
from .models import Patient  # importar el modelo Patient

admin.site.register(Patient)  # registrar modelo en admin
