from rest_framework import generics
from .models import PQRS
from .serializers import PQRSSerializer

class PqrListCreateView(generics.ListCreateAPIView):
    queryset = PQRS.objects.all()
    serializer_class = PQRSSerializer

class PqrRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQRS.objects.all()
    serializer_class = PQRSSerializer
