# Register your models here.
from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity',
                    'total_price', 'transaction_date', 'status')
    list_filter = ('status',)
    search_fields = ('customer__name', 'product__name')
