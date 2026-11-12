from django.shortcuts import render,redirect
from authentication_app.models import *
from authentication_app.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register_view(request):
    user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_view')

    context = {
            'title': 'Register',
            'button':'Register',
            'form_data': user_form
        }
    return render(request, 'master/baseform.html', context)

def login_view(request):
    user_form = AuthenticationForm()
    if request.method == 'POST':
        user_form = AuthenticationForm(request, data = request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            if user:
                login(request, user)
                return redirect('dashboard_view')

    context = {
        'title':'LOGIN',
        'button':'Login',
        'form_data': user_form
    }
    return render(request, 'master/baseform.html', context)

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout(request):
    logout(request)
    return redirect('register_view')