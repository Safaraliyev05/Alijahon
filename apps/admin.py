from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from apps.models import ProductProxy, CategoryProxy
from apps.models.proxy import DriverUserProxy, OperatorUserProxy, ManagerUserProxy, UserProxy, AdminUserProxy, \
    OrderProxy, NewOrderProxy, ReadyOrderProxy, DeliverOrderProxy, CantPhoneOrderProxy, \
    CanceledOrderProxy, ReturnedOrderProxy, ArchivedOrderProxy, HoldOrderProxy

site.unregister(Group)


class ProductNameMixin:
    def get_product_name(self, obj):
        return obj.product.name


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("usable_password", "password1", "password2"),
            },
        ),
    )
    ordering = ['phone']
    list_display = ['phone']


@register(ProductProxy)
class ProductProxyModelAdmin(ModelAdmin):
    list_display = ("id", "name")


@register(CategoryProxy)
class CategoryModelAdmin(ModelAdmin):
    list_display = ("id", "name")


@register(DriverUserProxy)
class DriverUserProxyAdmin(CustomUserAdmin):
    list_display = ("id",)


@register(OperatorUserProxy)
class OperatorUserProxyAdmin(CustomUserAdmin):
    pass


@register(ManagerUserProxy)
class ManagerUserProxyAdmin(CustomUserAdmin):
    pass


@register(UserProxy)
class UserProxyAdmin(CustomUserAdmin):
    pass


@register(AdminUserProxy)
class UserProxyAdmin(CustomUserAdmin):
    pass


@register(OrderProxy)
class OrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(NewOrderProxy)
class NewOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(ReadyOrderProxy)
class ReadyOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(DeliverOrderProxy)
class DeliverOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(CantPhoneOrderProxy)
class CantPhoneOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(CanceledOrderProxy)
class CanceledOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(ReturnedOrderProxy)
class ReturnedOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(ArchivedOrderProxy)
class ArchivedOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")


@register(HoldOrderProxy)
class HoldOrderProxyAdmin(ModelAdmin, ProductNameMixin):
    list_display = ("id", "get_product_name", "status")
