from django.urls import path
from .views import PatientListCreateView, PatientRetrieveUpdateDeleteView

urlpatterns = [
    path("", PatientListCreateView.as_view()),
    path("<int:pk>/", PatientRetrieveUpdateDeleteView.as_view()),
]
