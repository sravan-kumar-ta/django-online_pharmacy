from django.urls import path, include
from account import admin_views, customer_views
from medicines import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/', views.medicine, name='manage-medicine'),
    path('add_medicine/', views.add_medicine, name='add-medicine'),
    path('update_medicine/<int:m_id>/', views.update_medicine, name='update-medicine'),
    path('delete_medicine/<int:m_id>/', views.delete_medicine, name='delete-medicine'),

    # ####___admin aut urls___#### #
    path('account/', include('account.urls')),

    # ####___admin urls___#### #
    path('add_admin/', admin_views.add_admin, name='add-admin'),
    path('manage_admin/', admin_views.manage_admin, name='manage-admin'),
    path('update_admin/<int:admin_id>', admin_views.update_admin, name='update-admin'),
    path('delete_admin/<int:admin_id>', admin_views.delete_admin, name='delete-admin'),

    # ####___customer urls___#### #
    path('add_customer/', customer_views.add_customer, name='add-customer'),
    path('manage_customer/', customer_views.manage_customer, name='manage-customer'),
    path('update_customer/<int:customer_id>', customer_views.update_customer, name='update-customer'),
    path('delete_customer/<int:customer_id>', customer_views.delete_customer, name='delete-customer'),
]
