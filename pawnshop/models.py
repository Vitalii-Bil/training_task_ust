import decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(_("ім'я"), max_length=30)
    last_name = models.CharField(_("прізвище"), max_length=30)
    patronymic = models.CharField(_("по батькові"), max_length=30)
    phone_number = models.CharField(_("номер телефону"), max_length=100)
    email = models.EmailField(_('електронна пошта'), max_length=254)
    date_of_birth = models.DateField(_("дата народження"))
    passport_series = models.CharField(_("серія паспорту"), max_length=10)
    passport_number = models.CharField(_('номер паспорту'), max_length=30)
    passport_issued_by = models.CharField(_('ким виданий'), max_length=100)
    passport_valid_until = models.DateField(_("дійсний до"))
    registration = models.CharField(_('адреса приживання'), max_length=254)

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}"


class Material(models.Model):
    name = models.CharField(_("назва матеріалу"), max_length=100)
    content = models.IntegerField(_("проба"), validators=[MinValueValidator(0)])
    cost = models.DecimalField(
        _('ціна за грам (в гривнях)'),
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    class Meta:
        verbose_name = 'Матеріал'
        verbose_name_plural = 'Матеріали'

    def __str__(self):
        return f"{self.name} {self.content}"


class Good(models.Model):
    class GoodStatus(models.TextChoices):
        AWAITING_RANSOM = 'AS', _('очікує викупу')
        BELONG_TO_CLIENT = 'BC', _('належить клієнтові')
        BELONG_TO_PAWNSHOP = 'BP', _('належить ломбарду')
        SOLD_BY_LOMBARD = 'SL', _('продано ломбардом')

    name = models.CharField(_("назва товару"), max_length=100)
    description = models.CharField(_("опис"), max_length=255)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, verbose_name=_('матеріал'))
    weight = models.DecimalField(
        _('вага в грамах'),
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )
    status = models.CharField(
        _('статус товару'),
        max_length=2,
        choices=GoodStatus.choices,
        default=GoodStatus.AWAITING_RANSOM,
    )
    from_date = models.DateField(_("дата здачі"))
    redemption_time = models.DateField(_("кінцева дата викупу"))
    rate_field = models.DecimalField(
        _('відсоток на викуп (%)'),
        max_digits=3,
        decimal_places=0,
        default=decimal.Decimal(5),
        validators=PERCENTAGE_VALIDATOR
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_('клієнт'))
    first_delivery_price = models.DecimalField(_('ціна здачі (грн.)'), max_digits=8, decimal_places=2, null=True)
    first_redemption_price = models.DecimalField(_('ціна викупу (грн.)'), max_digits=8, decimal_places=2, null=True)

    @property
    def get_delivery_price(self):
        return f'{round(self.weight * self.material.cost, 2)}'
    get_delivery_price.fget.short_description = 'Ціна здачі станом на сьогодні (грн.)'

    @property
    def get_redemption_price(self):
        return f'{round(float(self.weight * self.material.cost) * 1.05, 2)}'
    get_redemption_price.fget.short_description = 'Ціна викупу станом на сьогодні (грн.)'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.first_delivery_price = round(self.weight * self.material.cost, 2)
            self.first_redemption_price = round(float(self.weight * self.material.cost) * 1.05, 2)
        super(Good, self).save(*args, **kwargs)
