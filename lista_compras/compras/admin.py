from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["nome", "quantidade", "comprado", "criado_em"]
    list_editable = ["comprado"]
    list_filter = ["comprado"]
    search_fields = ["nome"]