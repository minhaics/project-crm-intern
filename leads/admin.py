from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status',
                    'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('customer__name', 'product__name')

