from rest_framework import viewsets, permissions

from .serializers import RentSerializer
from .models import Rent

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticated]