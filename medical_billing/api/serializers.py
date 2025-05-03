from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Medicine, Bill

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active']
        read_only_fields = ['id']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'staff', 'medicine', 'quantity', 'packaging_type', 'total_price', 'created_at']


class LogoutSerializer(serializers.Serializer):
    message = serializers.CharField()


class SalesReportSerializer(serializers.Serializer):
    staff_username = serializers.CharField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)


class StockAvailabilitySerializer(serializers.Serializer):
    medicine_id = serializers.IntegerField()
    medicine_name = serializers.CharField()
    available_stock = serializers.IntegerField()
