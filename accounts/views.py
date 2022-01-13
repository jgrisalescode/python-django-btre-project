from django.shortcuts import redirect, render

def register(request):
    return render(request, template_name='accounts/register.html')

def login(request):
    return render(request, template_name='accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, template_name='accounts/dashboard.html')