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
        patient_name = request.POST.get('patient')  
        description = request.POST.get('description')  
        human = Patient.objects.get(name=patient_name)
        Symptom.objects.create(patient=human, description=description)
        return redirect('index')
    
    return render(request, 'add_symptom.html', {'humans': humans})

def add_service(request):
    humans = Patient.objects.all()  
    
    if request.method == 'POST':
        patient_name = request.POST.get('patient') 
        service_type = request.POST.get('service_type')
        human = Patient.objects.get(name=patient_name)
        Service.objects.create(patient=human, service_type=service_type)
        return redirect('index')
    
    return render(request, 'add_service.html', {'humans': humans})

def add_alert(request):
    humans = Patient.objects.all() 
    
    if request.method == 'POST':
        patient_name = request.POST.get('patient') 
        message = request.POST.get('message')
        human = Patient.objects.get(name=patient_name)
        Alert.objects.create(patient=human, message=message)
        return redirect('index')
    return render(request, 'add_alert.html', {'humans': humans})


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
    
    
    
    

    
   
