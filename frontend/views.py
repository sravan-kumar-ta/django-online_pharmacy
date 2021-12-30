from django.shortcuts import render
from medicines.models import Category


# Create your views here.
def home(request):
    categories = Category.objects.all()[:3]
    return render(request, 'frontend/pages/index.html', {'categories': categories})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'frontend/pages/categories.html', {'categories': all_categories})
