from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def analytics(request):
    return render(request, 'dashboard/analytics.html')

def statistics(request):
    return render(request, 'dashboard/statistics.html')