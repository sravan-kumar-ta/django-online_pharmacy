from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from account.EmailBackend import EmailBackEnd
from account.models import CustomUser


def register(request):
    if request.method != 'POST':
        return render(request, 'account/register.html')
    else:
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                               first_name=first_name, user_type=2)
        admin.save()
        return redirect('login')


def do_login(request):
    if request.method != 'POST':
        return render(request, 'account/login.html')
    else:
        try:
            user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                             password=request.POST.get("password"), user_type=str(2))
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid Login")
                return redirect('login')
        except:
            messages.error(request, "Invalid Login")
            return redirect('login')


def do_logout(request):
    logout(request)
    return redirect('login')
