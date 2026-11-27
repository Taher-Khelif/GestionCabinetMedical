from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Speciality(models.Model):
        name = models.CharField(max_length=50)
        class Meta:
            verbose_name = "Speciality"
            verbose_name_plural = "Specialities"
        def __str__(self):
            return f"{self.name}"
# Create your models here.
class User (AbstractUser):
    pass
number_validator = RegexValidator(regex=r'^\d{8}$', message='Compose exqctement de 8 chiffres.')

def birth_date_validator(date):
    if date >= timezone.localdate():
        raise ValidationError("La date de naissance ne peut pas être dans le futur.")

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone = models.CharField(max_length=8, unique=True, validators=[number_validator])
    specialities = models.ManyToManyField(Speciality, related_name='doctors')
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, unique=True, validators=[number_validator])
    birth_date = models.DateField(blank=True, validators=[birth_date_validator])
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    def __str__(self):
            return f"P. {self.first_name} {self.last_name}"

   