from django.shortcuts import redirect, render
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # Register user
        pass
    else:    
        return render(request, template_name='accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login user
        messages.error(request, 'User does not exists')
        return redirect('login')
    else:    
        return render(request, template_name='accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, template_name='accounts/dashboard.html')