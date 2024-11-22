# Register your models here.
from django.contrib import admin
from .models import SupportTicket


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'subject', 'status',
                    'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('customer__name', 'subject')
