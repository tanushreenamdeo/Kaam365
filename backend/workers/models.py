from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Worker(models.Model):
    WORKER_TYPES = [
        ('Plumber', 'Plumber'),
        ('Electrician', 'Electrician'),
        ('Carpenter', 'Carpenter'),
        ('Painter', 'Painter'),
        ('Helper', 'Helper'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    worker_type = models.CharField(max_length=50, choices=WORKER_TYPES)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, default='Male', blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)
    joined_date = models.DateField(default=date.today)
    location = models.CharField(max_length=100, default='Unknown')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.worker_type})"

class Project(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')
    start_date = models.DateField(default=date.today)
    completed_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    assigned_workers = models.ManyToManyField(Worker, blank=True, related_name='projects')

    def __str__(self):
        return self.name

class Payment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='payments')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.worker.name} - ₹{self.amount}"

class Schedule(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='schedules')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.worker.name} - {self.day} ({self.start_time}-{self.end_time})"
