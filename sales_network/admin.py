from django.contrib import admin

from sales_network.models import Network, Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['network', 'email', 'country', 'city', 'street', 'house']


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):

    def change_arrears(self, request, queryset):
        queryset.update(arrears=0)

    list_display = ['types_network', 'name', 'provider', 'arrears']
    list_filter = ['contact__city']
    list_display_links = ['provider']
    actions = ['change_arrears']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'model_product', 'date']
