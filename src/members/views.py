from django.shortcuts import redirect, render
from members.models import LoginForm, RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Register new user:
def register(request):
    
    if request.method == "GET":
        context = { "active": "register", "form":RegistrationForm() }
        return render(request, "register.html", context)
    
    form = RegistrationForm(request.POST)
    if not form.is_valid():
        context = { "active": "register", "form": form}
        return render(request, "register.html", context)
    
    user = form.save() # Save in database
    login(request, user) # Save user in server-side session
    messages.success(request, "Welcome " + user.first_name + "!")
    return redirect("home")

# Login view:
def log_in(request):
    
    if request.method == "GET":
        context = { "active": "login", "form": LoginForm() }
        return render(request, "login.html", context)
    
    form = LoginForm(request.POST)
    if not form.is_valid():
        context = {"active": "login", "form": form}
        return render(request, "login.html", context)
    
    # Check if username and password exists in db
    # Return the user if exists or None if not exists:
    user = authenticate(request, 
                        username = form.cleaned_data["email"], 
                        password = form.cleaned_data["password"])
    
    # If user does not exist:
    if not user:
        messages.error(request, "Incorrect email or password.")
        context = {"active": "login", "form": form}
        return render(request, "login.html", context)
    
    # User exists:
    login(request, user) # Save user in server-side session
    messages.success(request, "Welcome back " + user.first_name + "!")
    return redirect("home")

# Logout view:
def log_out(request):
    logout(request) # Remove the user from the server side session
    messages.error(request, "Bye Bye")
    return redirect("home")