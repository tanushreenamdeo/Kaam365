from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Worker, Project, Payment, Schedule

# HOME / LOGIN
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate with Django
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect("index")

        # Login the user
        login(request, user)

        # ADMIN LOGIN
        if role == "admin":
            if user.is_superuser:
                return redirect("admin_page")
            else:
                messages.error(request, "You are not an admin.")
                return redirect("index")

        # WORKER LOGIN
        try:
            worker = Worker.objects.get(user=user)
            return redirect("user_detail", worker_id=worker.id)
        except Worker.DoesNotExist:
            messages.error(request, "No worker profile linked to this account.")
            return redirect("index")

    return render(request, "index.html")



def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('index')


# REGISTER NEW WORKER (newuser)
def newuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        email = request.POST.get("email")
        worker_type = request.POST.get("worker_type")
        phone = request.POST.get("phone", "")
        location = request.POST.get("location", "")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("newuser")

        user = User.objects.create_user(username=username, password=password, email=email)
        Worker.objects.create(user=user, name=name, email=email, worker_type=worker_type, phone=phone, location=location)
        messages.success(request, "Account created successfully! Please login.")
        return redirect("index")

    return render(request, 'newuser.html')


# ADMIN DASHBOARD
def admin_page(request):
    workers = Worker.objects.all()
    projects = Project.objects.all()
    context = {
        'workers': workers,
        'total_workers': workers.count(),
        'total_projects': projects.count(),
        'total_completed': projects.filter(status='Completed').count(),
    }
    return render(request, 'admin.html', context)


# USER DETAIL (worker dashboard)
def user_detail(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    payments = Payment.objects.filter(worker=worker).order_by('-date')
    schedules = Schedule.objects.filter(worker=worker).order_by('day', 'start_time')
    return render(request, 'user.html', {'worker': worker, 'payments': payments, 'schedules': schedules})


# General pages
def overview(request):
    return render(request, 'overview.html')

def setting(request):
    return render(request, 'setting.html')


# Plumber pages (use data from workers)
def plumber(request):
    plumbers = Worker.objects.filter(worker_type='Plumber')
    return render(request, 'plumber.html', {'plumbers': plumbers})

def plumber_job_site(request):
    worker_id = request.GET.get('worker_id')
    worker = Worker.objects.filter(id=worker_id).first() if worker_id else None
    schedules = Schedule.objects.filter(worker=worker) if worker else []
    return render(request, 'plumber-job-site.html', {'worker': worker, 'schedules': schedules})

def plumber_payment(request):
    worker_id = request.GET.get('worker_id')
    worker = Worker.objects.filter(id=worker_id).first() if worker_id else None
    payments = Payment.objects.filter(worker=worker) if worker else []
    return render(request, 'plumber-payment.html', {'worker': worker, 'payments': payments})


# Electrician pages
def electrician(request):
    electricians = Worker.objects.filter(worker_type='Electrician')
    return render(request, 'electrician.html', {'electricians': electricians})

def electrician_job_site(request):
    worker_id = request.GET.get('worker_id')
    worker = Worker.objects.filter(id=worker_id).first() if worker_id else None
    schedules = Schedule.objects.filter(worker=worker) if worker else []
    return render(request, 'electrician-job-site.html', {'worker': worker, 'schedules': schedules})

def electrician_payment(request):
    worker_id = request.GET.get('worker_id')
    worker = Worker.objects.filter(id=worker_id).first() if worker_id else None
    payments = Payment.objects.filter(worker=worker) if worker else []
    return render(request, 'electrician-payment.html', {'worker': worker, 'payments': payments})


# Project pages
def active_project(request):
    projects = Project.objects.filter(status='Active')
    return render(request, 'ActiveProject.html', {'projects': projects})



def completed_projects(request):

    # Show ONLY the latest 5 completed projects
    projects = Project.objects.filter(status='Completed').order_by('-completed_date')[:5]

    # Extra counts for dashboard cards
    total_workers = Worker.objects.count()
    total_plumbers = Worker.objects.filter(worker_type='Plumber').count()
    total_electricians = Worker.objects.filter(worker_type='Electrician').count()

    return render(request, 'CompletedProjects.html', {
        'projects': projects,
        'total_workers': total_workers,
        'total_plumbers': total_plumbers,
        'total_electricians': total_electricians,
        'total_completed': projects.count(),   # Number of projects shown (max 5)
    })
