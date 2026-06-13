from django.shortcuts import render

# Create your views here.
def symptom_form(request):
    return render(request, 'diagnosis/symptom_form.html')

def diagnosis_result(request):
    return render(request, 'diagnosis/diagnosis_result.html')

def diagnosis_history(request):
    return render(request, 'diagnosis/diagnosis_history.html')

def report_pdf(request):
    # Placeholder for PDF generation logic
    return render(request, 'diagnosis/report_pdf.html')