from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Client, Good, Material


admin.site.unregister(Group)


def change_status_to_user(modeladmin, request, queryset):
    queryset.update(status="BC")


change_status_to_user.short_description = "Змінити статус на належить клієнтові"  # noqa:E305


def change_status_to_pawnshop(modeladmin, request, queryset):
    queryset.update(status="BP")


change_status_to_pawnshop.short_description = "Змінити статус на належить ломбарду"  # noqa:E305


def change_status_to_waiting(modeladmin, request, queryset):
    queryset.update(status="AS")


change_status_to_waiting.short_description = "Змінити статус на очікує викупу"  # noqa:E305


def change_status_to_sold(modeladmin, request, queryset):
    queryset.update(status="SL")


change_status_to_sold.short_description = "Змінити статус на продано лобмрдом"  # noqa:E305


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "description",
        "material",
        "weight",
        "rate_field",
        "status",
        "from_date",
        "redemption_time",
        "client",
        "first_delivery_price",
        "first_redemption_price",
        "get_delivery_price",
        "get_redemption_price",
    ]
    readonly_fields = ("first_delivery_price", "first_redemption_price", "get_delivery_price", "get_redemption_price")
    list_display = ("name", "status", "from_date", "redemption_time")
    list_filter = ("status", "client", "material")
    actions = [change_status_to_user, change_status_to_pawnshop, change_status_to_waiting, change_status_to_sold]
    search_fields = ["redemption_time"]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    fields = ["name", "content", "cost"]
    list_display = ("name", "content", "cost")
    list_filter = ("name",)


class ReadGoodInlineModelAdmin(admin.StackedInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""

    model = Good
    extra = 0
    show_change_link = True
    verbose_name = "Товар"
    verbose_name_plural = "Товари"
    fields = [
        "name",
        "description",
        "material",
        "weight",
        "rate_field",
        "status",
        "from_date",
        "redemption_time",
        "client",
        "first_delivery_price",
        "first_redemption_price",
        "get_delivery_price",
        "get_redemption_price",
    ]
    readonly_fields = ("first_delivery_price", "first_redemption_price", "get_delivery_price", "get_redemption_price")

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class AddGoodInlineModelAdmin(admin.StackedInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""

    model = Good
    extra = 0
    verbose_name = "Додати овар"
    verbose_name_plural = "Додати товари"

    exclude = ["first_delivery_price", "first_redemption_price"]

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = [
        "first_name",
        "last_name",
        "patronymic",
        "phone_number",
        "email",
        "date_of_birth",
        "passport_series",
        "passport_number",
        "passport_issued_by",
        "passport_valid_until",
        "registration",
    ]
    inlines = [ReadGoodInlineModelAdmin, AddGoodInlineModelAdmin]
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name", "phone_number", "passport_number")
    search_fields = ["first_name", "last_name", "passport_number", "phone_number"]
