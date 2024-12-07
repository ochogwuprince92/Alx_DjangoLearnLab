from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Registration form - extending UserCreationForm to add email
class customUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User Registration View
def register(request):
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # Fixed typo
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = customUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile Management View
@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
        messages.success(request, "Your profile has been updated")  # Fixed typo
        return redirect('profile')
    return render(request, 'blog/profile.html')

# Logout view using Django authentication
def user_logout(request):
    logout(request)
    return redirect('login')
