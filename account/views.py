from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from account.EmailBackEnd import EmailBackEnd


def register(request):
    if request.method != 'POST':
        return render(request, 'account/register.html')
    else:
        pass


def do_login(request):
    if request.method != 'POST':
        return render(request, 'account/login.html')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("<h1>Invalid Login</h1>")


def do_logout(request):
    logout(request)
    return redirect('login')