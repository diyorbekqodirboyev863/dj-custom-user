from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
# Home.
def home(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			...
	else:
		...
	if request.user.is_authenticated:
		return render(request, 'home.html', {'user': request.user})
	else:
		return render(request, 'home.html', {})

# Logout.
def logout(request):
	auth_logout(request)
	return redirect('home')

# Register.
def register(request):
	if request.method == 'POST':
		form = forms.CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			login(request, user)
			return redirect('home')
		else:
			...
	else:
		form = forms.CustomUserCreationForm()
	return render(request, 'register.html', {'form': form})