from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    path('user/', views.get_user)
]
