from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Speciality(models.Model):
        name = models.CharField(max_length=50)
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
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, unique=True, validators=[number_validator])
    birth_date = models.DateField(blank=True, validators=[birth_date_validator])

   