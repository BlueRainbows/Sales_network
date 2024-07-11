from django.urls import path
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from sales_network.apps import SalesNetworkConfig
from sales_network.views import NetworkViewSet, ContactViewSet, ProductViewSet

app_name = SalesNetworkConfig.name

networks_router = routers.SimpleRouter()
networks_router.register(r'contact', ContactViewSet, basename='contacts')
networks_router.register(r'network', NetworkViewSet, basename='networks')
networks_router.register(r'product', ProductViewSet, basename='products')

urlpatterns = [
    path(
        'login/',
        TokenObtainPairView.as_view(permission_classes=(permissions.AllowAny,)),
        name='login'
        ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(permission_classes=(permissions.AllowAny,)),
        name='token_refresh'
        )
] + networks_router.urls
