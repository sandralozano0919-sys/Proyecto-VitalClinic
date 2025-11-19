from django.db import models

class Schedule(models.Model):
    professional = models.ForeignKey("professionals.Professional", on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    color_code = models.CharField(max_length=7, default="#FFFFFF")
    status = models.CharField(max_length=20, default="LIBRE")

    def __str__(self):
        return f"{self.professional} - {self.date} {self.start_time}"

class Appointment(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    professional = models.ForeignKey("professionals.Professional", on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, null=True, blank=True, on_delete=models.SET_NULL)
    mode = models.CharField(max_length=10, choices=(("PRESENCIAL","Presencial"),("WEB","No presencial")))
    status = models.CharField(max_length=20, default="PROGRAMADA")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita {self.id} - {self.patient}"
