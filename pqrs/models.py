from django.db import models

class PQRS(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, default="PENDIENTE")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.subject}"
