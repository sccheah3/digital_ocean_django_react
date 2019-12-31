from django.urls import path

from customers import views

urlpatterns = [
    path('customers/', views.customers_list),
    path('customers/<int:pk>', views.customers_detail),
]
