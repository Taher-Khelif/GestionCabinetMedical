from django.contrib import admin

from AppointementApp.models import Appointment

@admin.register(Appointment)
class AppointmentAdminPersonaliser(admin.ModelAdmin):
    list_display = ( 'reason', 'status', )
    list_filter = ('status', )
