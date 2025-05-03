from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.models import Medicine, Bill
from .permissions import IsBillingStaff
from .serializers import BillSerializer


class CreateBillAPIView(APIView):
    permission_classes = [IsAuthenticated, IsBillingStaff]
    serializer_class = BillSerializer

    def post(self, request, *args, **kwargs):
        medicine_id = request.data.get('medicine_id')
        quantity = request.data.get('quantity')
        packaging_type = request.data.get('packaging_type')

        # Validate input
        if not all([medicine_id, quantity, packaging_type]):
            return JsonResponse({"error": "Missing required parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            medicine = Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return JsonResponse({"error": "Medicine not found"}, status=status.HTTP_404_NOT_FOUND)
        if medicine.stock_quantity < int(quantity):
            return JsonResponse({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST)

        # Map packaging_type to price field
        price_field_map = {
            'piece': medicine.price_piece,
            'strip': medicine.price_strip,
            'pack': medicine.price_pack,
            'box': medicine.price_box,
        }

        packaging_price = price_field_map.get(packaging_type)

        if packaging_price is None or packaging_price <= 0:
            return JsonResponse({"error": "Invalid packaging type or price not set"},
                                status=status.HTTP_400_BAD_REQUEST)

        # Calculate total price
        total_price = packaging_price * int(quantity)
        Bill.objects.create(
            staff=request.user,
            medicine=medicine,
            quantity=quantity,
            packaging_type=packaging_type,
            total_price=total_price
        )
        if medicine.stock_quantity >= quantity:
            medicine.stock_quantity -= int(quantity)
            medicine.save()
        else:
            return JsonResponse({"error": "Insufficient stock to complete the transaction"},
                                status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({
            "medicine_id": medicine_id,
            "quantity": quantity,
            "packaging_type": packaging_type,
            "total_price": float(total_price),
        }, status=status.HTTP_201_CREATED)
