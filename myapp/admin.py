from django.contrib import admin
from myapp.models import Patient, Symptom, Service

# Register your models here.
admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(Service)


