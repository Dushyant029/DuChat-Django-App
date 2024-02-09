# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

def landpage(request):
    return render(request, 'core/landpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('landpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')