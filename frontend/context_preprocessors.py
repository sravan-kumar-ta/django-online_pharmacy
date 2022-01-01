from frontend.models import Cart
from medicines.models import Category


def nav_categories(request):
    categories = Category.objects.all()
    context = {
        'categories_menu': categories,
    }
    return context


def cart_medicine(request):
    cart_medicines = Cart.objects.filter(user=request.user)
    return {'cart_medicines': cart_medicines}
