from django.contrib import admin
from django.urls import path,include
from coupons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coupon/list/', views.coupon_list),  
    path('coupon/create', views.create_coupon),
    path('coupon/edit/<int:id>/', views.edit_coupon),
    path('coupon/update/<int:id>/', views.update_coupon), 
    path('coupon/delete/<int:id>', views.delete_coupon),  
]