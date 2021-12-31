from django.shortcuts import render, get_object_or_404

from account.models import CustomUser


# Create your views here.
def manage_customer(request):
    customers = CustomUser.objects.all().filter(user_type=3).order_by("-id")
    return render(request, 'admin/customer/manage_customer.html', {'customers': customers})


def view_customer(request, customer_id):
    customer = get_object_or_404(CustomUser, id=customer_id)
    return render(request, 'admin/customer/customer.html', {'customer': customer})


def delete_customer(request, customer_id):
    pass
