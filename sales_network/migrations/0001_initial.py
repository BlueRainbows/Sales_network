# Generated by Django 5.0.7 on 2024-07-10 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('street', models.CharField(max_length=200, verbose_name='Улица')),
                ('house', models.CharField(max_length=200, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название сети')),
                ('types_network', models.PositiveIntegerField(choices=[(1, 'Завод'), (2, 'Pозничная сеть'), (3, 'Индивидуальный предприниматель')], verbose_name='Тип звена сети')),
                ('arrears', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Сумма задолженности')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales_network.contact', verbose_name='Название сети')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales_network.network')),
            ],
            options={
                'verbose_name': 'Сеть',
                'verbose_name_plural': 'Сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='Название продукта')),
                ('model_product', models.CharField(max_length=350, verbose_name='Модель продукта')),
                ('date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('name_network', models.ManyToManyField(to='sales_network.network', verbose_name='Название сети')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
