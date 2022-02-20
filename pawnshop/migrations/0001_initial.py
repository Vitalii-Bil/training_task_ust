# Generated by Django 4.0.2 on 2022-02-19 12:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name="ім'я")),
                ('last_name', models.CharField(max_length=30, verbose_name='прізвище')),
                ('patronymic', models.CharField(max_length=30, verbose_name='по батькові')),
                ('phone_number', models.CharField(max_length=100, verbose_name='номер телефону')),
                ('email', models.EmailField(max_length=254, verbose_name='електронна пошта')),
                ('date_of_birth', models.DateField(verbose_name='дата нарродження')),
                ('passport_series', models.CharField(max_length=10, verbose_name='серія паспорту')),
                ('passport_number', models.CharField(max_length=30, verbose_name='номер паспорту')),
                ('passport_issued_by', models.CharField(max_length=100, verbose_name='ким виданий')),
                ('passport_valid_until', models.DateField(verbose_name='дійсний до')),
                ('registration', models.CharField(max_length=254, verbose_name='адреса приживання')),
            ],
            options={
                'verbose_name': 'Клієнт',
                'verbose_name_plural': 'Клієнти',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='назва матеріалу')),
                ('content', models.CharField(max_length=300, verbose_name='проба')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='ціна за грам')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='назва товару')),
                ('description', models.CharField(max_length=255, verbose_name='опис')),
                ('weight', models.DecimalField(decimal_places=8, max_digits=8, verbose_name='вага')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='ціна сдачі')),
                ('status', models.CharField(choices=[('AS', 'очікує викупу'), ('BC', 'належить клієнтові'), ('BP', 'належить ломбарду')], default='AS', max_length=2, verbose_name='статус товару')),
                ('from_date', models.DateField(verbose_name='дата здачі')),
                ('redemption_time', models.IntegerField(validators=[django.core.validators.MaxValueValidator(365), django.core.validators.MinValueValidator(1)], verbose_name='термін викупу')),
                ('redemption_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='ціна викупу')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawnshop.client')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pawnshop.material')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
