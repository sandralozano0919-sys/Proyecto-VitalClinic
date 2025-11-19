from django.db import models
from django.conf import settings

class Professional(models.Model):
    # Relación con el usuario de Django
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="professional"
    )
    specialty = models.CharField(max_length=120)  # Ej: "Medicina General"
    license_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        # Muestra "Nombre Completo - Especialidad"
        return f"{self.user.get_full_name()} - {self.specialty}"
