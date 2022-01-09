from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from account.EmailBackend import EmailBackEnd
from account.models import CustomUser
from medicines.models import Category, Medicine


# Create your views here.
def home(request):
    categories = Category.objects.all()[:3]
    medicines = Medicine.objects.order_by('?')[:8]  # fetching random object
    return render(request, 'frontend/pages/index.html', {'categories': categories, 'medicines': medicines})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'frontend/pages/categories.html', {'categories': all_categories})


def add_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                  email=email, password=password, user_type=3)
        customer.save()
        messages.success(request, "Congratulations! Registration Successful!")
        return redirect('customer:registration')

    else:
        return render(request, 'frontend/pages/auth/register.html')


def do_login(request):
    if request.method != 'POST':
        return render(request, 'frontend/pages/auth/login.html')
    else:
        try:
            user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                             password=request.POST.get("password"), user_type=str(3))
            if user is not None:
                login(request, user)
                return redirect('customer:home')
            else:
                messages.error(request, "Invalid Login")
                return redirect('customer:login')
        except:
            messages.error(request, "Invalid Login")
            return redirect('customer:login')


def do_logout(request):
    logout(request)
    return redirect('customer:home')
