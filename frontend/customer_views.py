from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404, render

from medicines.models import Medicine, Category


def category_medicines(request, slug):
    category = get_object_or_404(Category, slug=slug)
    medicines = Medicine.objects.filter(is_active=True, category=category)
    all_categories = Category.objects.all()

    paginator = Paginator(medicines, 3)
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