from django.contrib import admin
from django.urls import path,include
from menus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Menu category path
    path('menu/category/list/', views.category_list),  
    path('menu/category/create/', views.create_category),
    path('menu/category/edit/<int:id>/', views.edit_category),
    path('menu/category/update/<int:id>/', views.update_category), 
    path('menu/category/delete/<int:id>', views.delete_category),  

    #Menu detail path
    path('menu/detail/list/', views.detail_list),  
    path('menu/detail/create/', views.create_detail),
    path('menu/detail/edit/<int:id>/', views.edit_detail),
    path('menu/detail/update/<int:id>/', views.update_details), 
    path('menu/detail/delete/<int:id>', views.delete_detail),  

     #Menu path
    path('menu/list/', views.menu_list),  
    path('menu/create/', views.create_menu),
    path('menu/edit/<int:id>/', views.edit_menu),
    path('menu/update/<int:id>/', views.update_menu), 
    path('menu/delete/<int:id>', views.delete_menu),  

]