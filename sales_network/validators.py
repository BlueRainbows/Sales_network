from rest_framework.serializers import ValidationError


class ArrearsValidator:

    def __init__(self, arrears):
        self.arrears = arrears

    def __call__(self, value):
        get_arrears = dict(value).get(self.arrears)
        if 0 > float(get_arrears):
            raise ValidationError(
                "Число не может быть отрицательным"
            )


class TypesNetworkValidator:

    def __init__(self, name, types_network, provider):
        self.name = name
        self.types_network = types_network
        self.provider = provider

    def __call__(self, value):
        get_name = dict(value).get(self.name)
        get_types_network = dict(value).get(self.types_network)
        get_provider = dict(value).get(self.provider)
        if get_provider:
            if get_types_network == 1 and get_provider.name != get_name:
                raise ValidationError(
                    "Завод может продавать только собственную продукцию"
                )
