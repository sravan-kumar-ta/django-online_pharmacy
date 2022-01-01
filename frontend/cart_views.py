import decimal

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from frontend.models import Cart
from medicines.models import Medicine


def cart(request):
    user = request.user
    cart_medicines = Cart.objects.filter(user=user)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user == user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.medicine.price)
            amount += temp_amount

    context = {
        'cart_medicines': cart_medicines,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
    }
    return render(request, 'frontend/pages/cart.html', context)


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
