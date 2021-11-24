from django.contrib import admin
from django.urls import path,include
from clients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #business type url
    path('business/type/list/', views.types_list),  
    path('business/type/create', views.create_types),
    path('business/type/edit/<int:id>/', views.edit_types),
    path('business/type/update/<int:id>/', views.update_type), 
    path('business/type/delete/<int:id>', views.delete_type), 

    # business owner url 
    path('business/owner/list/', views.owners_list),  
    path('business/owner/create', views.create_owners),
    path('business/owner/edit/<int:id>/', views.edit_owners),
    path('business/owner/update/<int:id>/', views.update_owner), 
    path('business/owner/delete/<int:id>', views.delete_owner), 

    # client url 
    path('client/list/', views.clients_list),  
    path('client/create', views.create_clients),
    path('client/edit/<int:id>/', views.edit_clients),
    path('client/update/<int:id>/', views.update_client), 
    path('client/delete/<int:id>', views.delete_client), 

]