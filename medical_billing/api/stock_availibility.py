from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.serializers import StockAvailabilitySerializer
from core.models import Medicine


class StockAvailabilityAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = StockAvailabilitySerializer

    def get(self, request, *args, **kwargs):
        # Fetch all medicines with their stock quantity
        medicines = Medicine.objects.all().values('name', 'stock_quantity')

        return Response({"stock": list(medicines)}, status=200)
