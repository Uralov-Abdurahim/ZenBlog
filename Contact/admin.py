from django.contrib import admin
from Contact.models import Information, Contact

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'email')
    list_display_links = ('address', 'phone_number', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    list_display_links = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'subject', 'created_at')
    list_filter = ('created_at',)