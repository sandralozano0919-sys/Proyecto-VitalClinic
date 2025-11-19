from rest_framework import serializers
from .models import Appointment, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
