from django.shortcuts import render
from rest_framework import generics
from .models import Appointment, Schedule
from .serializers import AppointmentSerializer, ScheduleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Vista para servir el template
def index(request):
    return render(request, 'index.html', {'test': '¡Funciona!'})

# API para appointments
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        # Obtiene el paciente desde el usuario autenticado
        patient = self.request.user.patient

        # Guarda la cita asignando automáticamente al paciente
        serializer.save(patient=patient)

# API para schedules
class ScheduleListCreateView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# Endpoint para FullCalendar
class ScheduleEventsView(APIView):
    def get(self, request):
        schedules = Schedule.objects.all()
        events = []

        for schedule in schedules:
            events.append({
                "id": schedule.id,
                "title": f"Prof {schedule.professional.id} - {schedule.status}",
                "start": f"{schedule.date}T{schedule.start_time}",
                "end": f"{schedule.date}T{schedule.end_time}",
                "color": schedule.color_code
            })
        return Response(events)

