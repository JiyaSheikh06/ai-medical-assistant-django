from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'accounts/login.html')
def logout(request):
       return HttpResponse("You have been logged out.")
def profile(request):
    return render(request, 'accounts/profile.html')
def register(request):
    return render(request, 'accounts/register.html')