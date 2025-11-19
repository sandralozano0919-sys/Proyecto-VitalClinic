from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListCreateView.as_view(), name='appointments'),  # /api/appointments/
    path('schedules/', views.ScheduleListCreateView.as_view(), name='schedules'),  # /api/appointments/schedules/
    path('events/', views.ScheduleEventsView.as_view(), name='schedule-events'),  # /api/appointments/events/
]
