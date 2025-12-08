from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    stroke_history = models.BooleanField()
    medication = models.TextField()
    phone_number = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Symptom(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Symptom for {self.patient.name} reported on {self.date_reported}"

class Service(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    date_received = models.DateField(auto_now_add=True)
   
    def __str__(self):
       return f"{self.service_type} for {self.patient.name}"

    
class Alert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Alert for {self.patient.name} created on {self.date_created}")