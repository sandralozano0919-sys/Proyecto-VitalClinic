from django.urls import path
from .views import PqrListCreateView, PqrRetrieveUpdateDeleteView

urlpatterns = [
    path("", PqrListCreateView.as_view(), name="pqr-list-create"),
    path("<int:pk>/", PqrRetrieveUpdateDeleteView.as_view(), name="pqr-detail"),
]
