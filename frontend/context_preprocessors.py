from medicines.models import Category


def nav_categories(request):
    categories = Category.objects.all()
    context = {
        'categories_menu': categories,
    }
    return context
