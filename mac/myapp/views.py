from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse


def index_view(request):
    return render(request, 'index.html')



@login_required(login_url='registration')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def registration_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if action == 'register':
            full_name = request.POST.get('full_name', '').strip()

            if User.objects.filter(username=email).exists():
                messages.error(request, 'An account with this email already exists.')
                return redirect('registration')

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name,
            )
            login(request, user)
            return redirect('dashboard')

        if action == 'login':
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

            messages.error(request, 'Credentials not found. Please register.')
            return redirect(f"{reverse('registration')}?tab=register")

    return render(request, 'registration.html')

    
def students_view(request):
    return render(request, 'students.html')

def addstudents_view(request):
    return render(request, 'addstudents.html')