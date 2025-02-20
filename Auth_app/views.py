from django.shortcuts import render
from django.contrib import messages, auth
from .models import user_data
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserDataForm

def user_signup(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            
            #create user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            
            
            return redirect('login')  # Redirect to a success page
    else:
        form = UserDataForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    else:
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username)
        print(password)
        
        if username and password:
            user = auth.authenticate(username=username,password=password)
            
            if user:        
                auth.login(request,user)
                print("User logged in")
                messages.success(request,'Welcome, '+user.username+' you are now logged in')
                return redirect('dashboard')
                
            
            messages.error(request,'Invalid credentials, try again')
            return render(request,'authentication/login.html')
        
        messages.error(request,'Please fill all fields')
        return render(request,'authentication/login.html')
    

def dashboard(request):
    
    user_info = user_data.objects.filter(username=request.user.username)
    print(user_info)
    return render(request, 'authentication/dashboard.html', {'user_info': user_info})

def user_logout(request):
    auth.logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')
    