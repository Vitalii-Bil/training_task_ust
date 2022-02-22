# Generated by Django 4.0.2 on 2022-02-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0002_alter_good_first_delivery_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='first_delivery_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='ціна здачі'),
        ),
        migrations.AlterField(
            model_name='good',
            name='first_redemption_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='ціна викупу'),
        ),
    ]