from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Sum

from api.serializers import SalesReportSerializer
from core.models import Bill
from datetime import datetime


class SalesReportAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SalesReportSerializer

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Start date and end date are required"}, status=400)

        try:
            # Parse the dates
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Please use YYYY-MM-DD."}, status=400)

        # Fetch sales reports: Group by staff and filter by date range
        sales_report = Bill.objects.filter(created_at__range=[start_date, end_date]) \
            .values('staff__username') \
            .annotate(total_sales=Sum('total_price')) \
            .order_by('-total_sales')

        return Response({"sales_report": list(sales_report)}, status=200)
