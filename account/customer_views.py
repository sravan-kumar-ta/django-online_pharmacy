from django.shortcuts import render, get_object_or_404, redirect

from account.models import CustomUser
from frontend.models import Order


# Create your views here.
def manage_customer(request):
    customers = CustomUser.objects.all().filter(user_type=3).order_by("-id")
    return render(request, 'admin/customer/manage_customer.html', {'customers': customers})


def view_customer(request, customer_id):
    customer = get_object_or_404(CustomUser, id=customer_id)
    order_list = Order.objects.filter(user=customer_id).order_by('-id')
    return render(request, 'admin/customer/customer.html', {'customer': customer, 'order_list': order_list})


def delete_customer(request, customer_id):
    customer = get_object_or_404(CustomUser, id=customer_id)
    customer.delete()
    return redirect('manage-customer')
