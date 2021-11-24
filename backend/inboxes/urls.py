from django.contrib import admin
from django.urls import path,include
from inboxes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inbox/list/', views.inbox_list),  
    path('inbox/create', views.create_inbox),
    path('inbox/edit/<int:id>/', views.edit_inbox),
    path('inbox/update/<int:id>/', views.update_inbox), 
    path('inbox/delete/<int:id>', views.delete_inbox),  

]