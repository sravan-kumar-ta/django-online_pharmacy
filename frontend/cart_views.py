from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from frontend.models import Cart
from medicines.models import Medicine


def cart(request):
    user = request.user
    cart_medicines = Cart.objects.filter(user=user)
    return render(request, 'frontend/pages/cart.html', {'cart_medicines': cart_medicines})


def add_cart(request):
    user = request.user
    medicine_id = request.GET.get('medicine_id')
    medicine = get_object_or_404(Medicine, id=medicine_id)

    item_already_in_cart = Cart.objects.filter(medicine=medicine_id, user=user)
    if item_already_in_cart:
        cart_medicines = get_object_or_404(Cart, medicine=medicine_id, user=user)
        cart_medicines.quantity += 1
        cart_medicines.save()
    else:
        Cart(user=user, medicine=medicine).save()

    return redirect('customer:cart')


def remove_cart(request, cart_id):
    if request.method == 'GET':
        medicine = get_object_or_404(Cart, id=cart_id)
        medicine.delete()
        messages.success(request, "Medicine removed from Cart.")
    return redirect('customer:cart')


def plus_cart(request, cart_id):
    if request.method == 'GET':
        medicine = get_object_or_404(Cart, id=cart_id)
        medicine.quantity += 1
        medicine.save()
    return redirect('customer:cart')


def minus_cart(request, cart_id):
    if request.method == 'GET':
        medicine = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if medicine.quantity == 1:
            medicine.delete()
        else:
            medicine.quantity -= 1
            medicine.save()
    return redirect('customer:cart')
