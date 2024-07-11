from django.db import models

PROVIDERS = [
    (1, 'Завод'),
    (2, 'Pозничная сеть'),
    (3, 'Индивидуальный предприниматель')
]


class Contact(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта'
    )
    country = models.CharField(
        max_length=200,
        verbose_name='Страна'
    )
    city = models.CharField(
        max_length=200,
        verbose_name='Город'
    )
    street = models.CharField(
        max_length=200,
        verbose_name='Улица'
    )
    house = models.CharField(
        max_length=200,
        verbose_name='Номер дома'
    )

    def __str__(self):
        return (f'Электронная почта: {self.email}. '
                f'Адрес: {self.country}, {self.city}, {self.street}, {self.house}')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'


class Network(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название сети'
    )
    types_network = models.PositiveIntegerField(
        choices=PROVIDERS,
        verbose_name='Тип звена сети',
    )
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Поставщик'
    )
    arrears = models.DecimalField(
        decimal_places=2,
        default=0.00,
        max_digits=15,
        verbose_name='Сумма задолженности'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        verbose_name='Контактная информация'
    )

    def __str__(self):
        return f'Название организации: {self.name}'

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'


class Product(models.Model):
    name_network = models.ManyToManyField(
        Network,
        verbose_name='Реализаторы'
    )
    product_name = models.CharField(
        max_length=200,
        verbose_name='Название продукта'
    )
    model_product = models.CharField(
        max_length=350,
        verbose_name='Модель продукта'
    )
    date = models.DateField(
        verbose_name='Дата выхода продукта на рынок'
    )

    def __str__(self):
        return (f'Название продукта: {self.product_name}. '
                f'Модель продукта: {self.model_product}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
