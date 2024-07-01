from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_Home,name='Product_Home'),
    path('All_product/', views.Product_list,name='Product_list'),
    path('list/<pk>',views.Product_list_one,name='Product_list_one'),
    path('search/', views.product_search, name='product_search'),

    # path('edit/<pk>', views.edit,name='edit'),
    # path('delete/<pk>', views.delete,name='delete'),
]