# //forms.py
from django import forms
from .models import Patient, Doctor, Nurse, EPHI, Insurance

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'

class EPHIForm(forms.ModelForm):
    class Meta:
        model = EPHI
        fields = '__all__'

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
