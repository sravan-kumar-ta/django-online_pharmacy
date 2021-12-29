from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from medicines.models import Category, Medicine


# Create your views here.
def home(request):
    categories = Category.objects.all()[:3]
    return render(request, 'frontend/pages/index.html', {'categories': categories})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'frontend/pages/categories.html', {'categories': all_categories})


def category_medicines(request, slug):
    category = get_object_or_404(Category, slug=slug)
    medicines = Medicine.objects.filter(is_active=True, category=category)
    all_categories = Category.objects.all()

    context = {
        'category': category,
        'medicines': medicines,
        'categories': all_categories,
    }
    return render(request, 'frontend/pages/category_products.html', context)
