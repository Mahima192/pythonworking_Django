from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),
    path('create/doctor/', doctor_create, name='doctor_create'),
    path('update/doctor/<int:pk>/', doctor_update, name='doctor_update'),
    path('delete/doctor/<int:pk>/', doctor_delete, name='doctor_delete'),
    path('create/nurse/', nurse_create, name='nurse_create'),
    path('update/nurse/<int:pk>/', nurse_update, name='nurse_update'),
    path('delete/nurse/<int:pk>/', nurse_delete, name='nurse_delete'),
    path('create/ephi/', ephi_create, name='ephi_create'),
    path('update/ephi/<int:pk>/', ephi_update, name='ephi_update'),
    path('delete/ephi/<int:pk>/', ephi_delete, name='ephi_delete'),
    path('create/insurance/', insurance_create, name='insurance_create'),
    path('update/insurance/<int:pk>/', insurance_update, name='insurance_update'),
    path('delete/insurance/<int:pk>/', insurance_delete, name='insurance_delete'),
    path('create/patient/', patient_create, name='patient_create'),
    path('update/patient/<int:pk>/', patient_update, name='patient_update'),
    path('delete/patient/<int:pk>/', patient_delete, name='patient_delete'),
]
