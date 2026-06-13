from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.patient_profile, name='patient_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('history/', views.medical_history, name='medical_history'),
]