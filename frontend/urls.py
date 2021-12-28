from django.urls import path
from frontend import views

app_name = 'customer'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/', views.category, name='category')
]
