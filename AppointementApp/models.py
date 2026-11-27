from django.db import models    
from django.core.validators import FileExtensionValidator
from AccountApp.models import Doctor, Patient
from django.utils import timezone
from django.core.exceptions import ValidationError

class Appointment(models.Model):
    reason = models.TextField(max_length=255)
    prescription = models.FileField(upload_to='prescriptions/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed.')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
duration_minutes = models.PositiveIntegerField(default=30)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
doctor = models.ForeignKey(Doctor, related_name='Appointments', on_delete=models.CASCADE)
patient = models.ForeignKey(Patient, related_name='Appointments', on_delete=models.CASCADE)
appointment_date = models.DateTimeField(blank=False)
def clean(self):
    modified_date = self._state.adding or(
        Appointment.objects.filter(pk=self.pk, appointment_date=self.appointment_date).exists()
    )
    if self.appointment_date <= timezone.localdate():
        raise ValidationError("Appointment date cannot be in the past.")
class Meta:
    ordering = ['appointment_date']
    constraints = [
        models.UniqueConstraint(fields=['doctor', 'appointment_date'], name='unique_doctor_appointment', violation_error_message="This doctor already has an appointment at this date and time."),
    ]
def __str__(self):
        return f"{self.reason}"