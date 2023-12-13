# views.py

from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login 
from .models import Doctor, Patient, Nurse , EPHI, Insurance
from .forms import DoctorForm, NurseForm , EPHIForm, InsuranceForm, PatientForm

def index(request):
    return render(request, 'index.html', {})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the list view after successful creation
    else:
        form = DoctorForm()

    return render(request, 'doctor_create.html', {'form': form})

def is_doctor(user):
    return user.groups.filter(name='Doctor').exists()

def is_patient(user):
    return user.groups.filter(name='Patient').exists()

@login_required(login_url='login')
def dashboard(request):
    if is_doctor(request.user):
        doctors = Doctor.objects.all()
        return render(request, 'index.html', {'doctors': doctors})
    elif is_patient(request.user):
        patient = Patient.objects.get(user=request.user)
        return render(request, 'index.html', {'patient': patient})
    else:
        # Handle other user types or unauthorized access
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('dashboard')  # Redirect to the dashboard or any other page after successful login
        else:
            # Authentication failed, show an error message or handle it as needed
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

# Doctor views
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('index')  # Update with your desired redirect URL

@login_required(login_url='login')
def doctor_dashboard(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})
@login_required(login_url='login')
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, 'index.html', {'patient': patient})
# Nurse views
def nurse_create(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = NurseForm()
    return render(request, 'nurse_form.html', {'form': form})

def nurse_update(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    if request.method == 'POST':
        form = NurseForm(request.POST, instance=nurse)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = NurseForm(instance=nurse)
    return render(request, 'nurse_form.html', {'form': form})

def nurse_delete(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    nurse.delete()
    return redirect('index')  # Update with your desired redirect URL
# EPHI views
def ephi_create(request):
    if request.method == 'POST':
        form = EPHIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = EPHIForm()
    return render(request, 'ephi_form.html', {'form': form})

def ephi_update(request, pk):
    ephi = get_object_or_404(EPHI, pk=pk)
    if request.method == 'POST':
        form = EPHIForm(request.POST, instance=ephi)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = EPHIForm(instance=ephi)
    return render(request, 'ephi_form.html', {'form': form})

def ephi_delete(request, pk):
    ephi = get_object_or_404(EPHI, pk=pk)
    ephi.delete()
    return redirect('index')  # Update with your desired redirect URL

# Insurance views
def insurance_create(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = InsuranceForm()
    return render(request, 'insurance_form.html', {'form': form})

def insurance_update(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = InsuranceForm(instance=insurance)
    return render(request, 'insurance_form.html', {'form': form})

def insurance_delete(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    insurance.delete()
    return redirect('index')  # Update with your desired redirect URL

# Patient views
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('index')  # Update with your desired redirect URL
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('index') 