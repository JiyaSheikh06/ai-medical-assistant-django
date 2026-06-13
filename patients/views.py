from django.shortcuts import render
from django.http import HttpResponse


def patient_profile(request):
    return render(request, 'patients/profile.html') 

def edit_profile(request):
    return render(request, 'patients/edit_profile.html')    

def medical_history(request):
    return render(request, 'patients/medical_history.html')
