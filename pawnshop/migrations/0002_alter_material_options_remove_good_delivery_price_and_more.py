# Generated by Django 4.0.2 on 2022-02-20 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Матеріал', 'verbose_name_plural': 'Матеріали'},
        ),
        migrations.RemoveField(
            model_name='good',
            name='delivery_price',
        ),
        migrations.RemoveField(
            model_name='good',
            name='redemption_price',
        ),
        migrations.AlterField(
            model_name='good',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawnshop.client', verbose_name='клієнт'),
        ),
        migrations.AlterField(
            model_name='good',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pawnshop.material', verbose_name='матеріал'),
        ),
        migrations.AlterField(
            model_name='good',
            name='weight',
            field=models.FloatField(verbose_name='вага в грамах'),
        ),
    ]
