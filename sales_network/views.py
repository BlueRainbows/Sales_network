from rest_framework import viewsets
from django_filters import rest_framework as filters

from sales_network.models import Network, Contact, Product
from sales_network.serializers import NetworkSerializer, ContactSerializer, ProductSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contact__country',)

    def perform_update(self, serializer):
        network = Network.objects.get(pk=self.get_object().pk)
        serializer.save(arrears=network.arrears)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country',)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
