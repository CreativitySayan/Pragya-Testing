from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'participant_name', 'event_name', 'date')
    search_fields = ('certificate_number', 'participant_name', 'event_name')
