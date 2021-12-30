from django.urls import path
from frontend import views, customer_views

app_name = 'customer'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('<slug:slug>/', customer_views.category_medicines, name="medicine-list"),
]
