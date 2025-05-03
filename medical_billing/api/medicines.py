from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Medicine
from .permissions import IsInventoryManager
from .serializers import MedicineSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated, IsInventoryManager]
