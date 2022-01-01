from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404, render

from medicines.models import Medicine, Category
from .models import Order


def category_medicines(request, slug):
    category = get_object_or_404(Category, slug=slug)
    medicines = Medicine.objects.filter(is_active=True, category=category)
    all_categories = Category.objects.all()

    paginator = Paginator(medicines, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        medicines_by_page = paginator.page(page)
    except(EmptyPage, InvalidPage):
        medicines_by_page = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'medicines': medicines_by_page,
        'categories': all_categories,
    }
    return render(request, 'frontend/pages/category_products.html', context)


def detail_of_medicines(request, c_slug, m_slug):
    medicine = get_object_or_404(Medicine, slug=m_slug)
    related_medicines = Medicine.objects.exclude(id=medicine.id).filter(is_active=True, category__slug=c_slug)

    context = {
        'medicine': medicine,
        'related_medicines': related_medicines,
    }
    return render(request, 'frontend/pages/detail.html', context)


def profile(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    return render(request, 'frontend/pages/auth/profile.html', {'orders': orders})
