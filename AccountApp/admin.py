from django.contrib import admin

from AccountApp.models import User, Doctor, Patient, Speciality



admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Speciality)
