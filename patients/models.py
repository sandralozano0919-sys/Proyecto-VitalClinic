from django.db import models
from django.conf import settings

class Patient(models.Model):
    # Relación con el usuario de Django
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Datos personales
    documento_num = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100, default="Paciente")
    last_name = models.CharField(max_length=100, default="Prueba")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    eps = models.CharField(max_length=120, blank=True)
    
    # Fecha de creación automática
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.documento_num}"

