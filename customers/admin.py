from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address',
                    'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
