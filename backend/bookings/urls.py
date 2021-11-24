from django.contrib import admin
from django.urls import path,include
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/list/', views.bookings_list),  
    path('booking/create', views.create_booking),
    path('booking/edit/<int:id>/', views.edit_booking),
    path('booking/update/<int:id>/', views.update_booking), 
    path('booking/delete/<int:id>', views.delete_booking),  

]