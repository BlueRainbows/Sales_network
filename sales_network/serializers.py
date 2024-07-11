from rest_framework import serializers
from sales_network.models import Network, Contact, Product
from sales_network.validators import ArrearsValidator, TypesNetworkValidator


class ContactSerializer(serializers.ModelSerializer):
    network = serializers.SerializerMethodField(read_only=True)

    def get_network(self, contact):
        if Network.objects.filter(contact__id=contact.id).exists():
            network = Network.objects.get(contact__id=contact.id)
            return network.name
        else:
            network = "Сеть не указана"
            return network

    class Meta:
        model = Contact
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)

    def get_products(self, network):
        if Product.objects.filter(name_network__id=network.id).exists():
            prod_list = []
            products = Product.objects.filter(name_network__id=network.id)
            for prod in products:
                str_prod = str(prod.pk) + ' ' + prod.product_name + ' ' + prod.model_product
                prod_list.append(str_prod)
            return prod_list
        else:
            products = "Сеть не реализует продукты"
            return products

    class Meta:
        model = Network
        fields = '__all__'
        validators = [
            ArrearsValidator(
                arrears='arrears'
            ),
            TypesNetworkValidator(
                name='name',
                types_network='types_network',
                provider='provider'
            )
        ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
