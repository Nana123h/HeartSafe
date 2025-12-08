from django.contrib import admin
from myapp.models import Patient, Symptom, Service, Alert  

# Register your models here.
admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(Service)
admin.site.register(Alert)

