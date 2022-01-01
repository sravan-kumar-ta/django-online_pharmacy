from django.urls import path
from frontend import views, customer_views, cart_views

app_name = 'customer'

urlpatterns = [
    # ###--cart_views.py--###
    path('cart/', cart_views.cart, name="cart"),
    path('add_cart/', cart_views.add_cart, name="add-to-cart"),
    path('plus-cart/<int:cart_id>/', cart_views.plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>/', cart_views.minus_cart, name="minus-cart"),
    path('remove-cart/<int:cart_id>/', cart_views.remove_cart, name="remove-cart"),
    path('checkout/', cart_views.checkout, name='checkout'),

    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('sign_up/', views.add_customer, name="registration"),
    path('log_in/', views.do_login, name="login"),
    path('log_out/', views.do_logout, name="logout"),

    # ###--customer_views.py--###
    path('profile/', customer_views.profile, name='profile'),
    path('<slug:slug>/', customer_views.category_medicines, name="medicine-list"),
    path('<slug:c_slug>/<slug:m_slug>/', customer_views.detail_of_medicines, name="medicine-detail"),
]
