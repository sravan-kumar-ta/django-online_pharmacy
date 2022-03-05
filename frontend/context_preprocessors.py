from frontend.models import Cart
from medicines.models import Category


def nav_categories(request):
    categories = Category.objects.all()
    context = {
        'categories_menu': categories,
    }
    return context


def cart_medicine(request):
    if request.user.is_authenticated:
        cart_medicines = Cart.objects.filter(user=request.user)
        return {'cart_medicines': cart_medicines}
    else:
        cart_medicines = Cart.objects.all()
        return {'cart_medicines': cart_medicines}
