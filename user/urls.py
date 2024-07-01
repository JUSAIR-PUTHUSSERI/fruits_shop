from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('login/', views.user_login, name='login'),  # Updated to match the renamed view
    path('logout/', views.user_logout, name='logout'),  # Updated to match the renamed view
   
]
