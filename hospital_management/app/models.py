from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICES)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

class Nurse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Nurse {self.first_name} {self.last_name}"

class EPHI(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Insurance(models.Model):
    name = models.CharField(max_length=255)
    coverage_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    