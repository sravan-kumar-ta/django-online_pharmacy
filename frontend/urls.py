from django.urls import path
from frontend import views

app_name = 'customer'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('<slug:slug>/', views.category_medicines, name="medicine-list"),
]
