from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .accounts import RegisterView, LogoutView
from .billing import CreateBillAPIView
from .medicines import MedicineViewSet
from .sales_report import SalesReportAPIView
from .stock_availibility import StockAvailabilityAPIView
from .users import UserListView, UserDetailView

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet, basename='medicine')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view()),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
    path('billing/', CreateBillAPIView.as_view(), name='medicine-billing'),
    path('dashboard/stock/', StockAvailabilityAPIView.as_view(), name='stock-availability'),
    path('dashboard/reports/', SalesReportAPIView.as_view(), name='sales-report'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Generates the OpenAPI schema
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
