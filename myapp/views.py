from django.shortcuts import render,redirect
from django_daraja.mpesa.core import MpesaClient
from .models import Patient, Symptom, Service, Alert    

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def doctors(request):
    return render(request, 'doctors.html')  
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')

# dashboard functions
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        stroke_history = request.POST.get('stroke_history') == 'on'
        medication = request.POST.get('medication') 
        phone_number = request.POST.get('phone_number') 
        Patient.objects.create(name=name,age=age,gender=gender,stroke_history=stroke_history,medication=medication,  
        phone_number=phone_number)
        return redirect('index')
    return render(request, 'add_patient.html')  
def add_symptom(request):
    humans = Patient.objects.all()
    if request.method == 'POST':
       patient_id = request.POST.get('patient_id') 
       patient = Patient.objects.get(id=patient_id)
       description = request.POST.get('description')
       Symptom.objects.create(patient=patient,description=description)
       return redirect('index')
    return render(request, 'add_symptom.html',{'humans':humans})
def add_service(request):
    humans = Patient.objects.all()
    if request.method == 'POST':
       patient_id = request.POST.get('patient_id') 
       patient = Patient.objects.get(id=patient_id)
       service_type = request.POST.get('service_type')
       Service.objects.create(patient=patient,service_type=service_type)
       return redirect('index')
    return render(request, 'add_service.html',{'humans':humans})
def add_alert(request):
    humans = Patient.objects.all()
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id') 
        patient = Patient.objects.get(id=patient_id)
        message = request.POST.get('message')
        Alert.objects.create( patient=patient,message=message)
        return redirect('index')
    return render(request, 'add_alert.html',{'humans':humans})

def payment(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amount'))
        
        client = MpesaClient()
        
        account_ref ='HeartSafe'
        desc = 'support services payment'
        
        callback_url = 'https://callback.com/url'
        
        response = client.stk_push(
            phone_number=phone,
            amount=amount,
            account_reference=account_ref,
            transaction_desc=desc,
            callback_url=callback_url
        )
        return render(request, "HeartSafe_Payment.html", {"message":"STK Push sent!"})
    return render(request, 'HeartSafe_Payment.html')
    
    
    
    

    
   
