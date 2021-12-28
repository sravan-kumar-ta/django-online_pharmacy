from django.http import HttpResponse
from django.shortcuts import render
from medicines.models import Category


# Create your views here.
def home(request):
    categories = Category.objects.all()[:3]
    return render(request, 'frontend/pages/index.html', {'categories': categories})


def category(requset):
    pass