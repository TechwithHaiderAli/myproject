from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm  
from django.contrib.auth import logout
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # Perform actions, e.g., save the form data to the database
            form.save()  # Assuming you have a model tied to the form
            # Redirect to a success page or somewhere else
            return redirect('success')  # Replace 'success' with your actual success view name
        else:
            # If form is invalid, render the registration page with form errors
            return render(request, 'users/register.html', {'form': form})

    # If it's a GET request, display an empty form
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:list')  # Redirect to home page after login
            else:
                form.add_error(None, 'Invalid credentials')  # Optionally add error
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('/') 

