from django.urls import path
from . import views

urlpatterns = [
    path('symptoms/', views.symptom_form, name='symptom_form'),
    path('result/', views.diagnosis_result, name='diagnosis_result'),
    path('history/', views.diagnosis_history, name='diagnosis_history'),
    path('report/', views.report_pdf, name='report_pdf'),
]