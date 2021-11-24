from django.contrib import admin
from django.urls import path,include
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/list', views.orders_list),  
    path('order/create/', views.create_order),
    path('order/edit/<int:id>/', views.edit),
    path('order/update/<int:id>/', views.update_order), 
    path('order/delete/<int:id>', views.delete_order),  

]