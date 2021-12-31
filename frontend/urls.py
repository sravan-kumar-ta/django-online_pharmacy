from django.urls import path
from frontend import views, customer_views

app_name = 'customer'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('sign_up/', views.add_customer, name="registration"),
    path('log_in/', views.do_login, name="login"),
    path('log_out/', views.do_logout, name="logout"),

    path('<slug:slug>/', customer_views.category_medicines, name="medicine-list"),
]
