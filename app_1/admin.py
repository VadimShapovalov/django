from django.contrib import admin

from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name']
    search_help_text = 'Поиск по полю "name".'


@admin.action(description='Сбросить количество до нуля')
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'price', 'amount']

    """Отдельный продукт."""
    readonly_fields = ['date']

    ordering = ['price', '-amount']
    search_fields = ['description']
    search_help_text = 'Поиск по полю "Описание продукта (description)".'
    actions = [reset_amount]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Прочие данные о товаре',
                'fields': ['date', 'photo'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'date_created', 'total_price']
    ordering = ['date_created', 'total_price']
    list_filter = ['date_created', 'total_price']
    search_fields = ['client']
    search_help_text = 'Поиск по полю "client".'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
