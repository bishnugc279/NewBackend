from django.contrib import admin
from django.urls import path,include
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/list/', views.review_list),  
    path('review/create', views.create_review),
    path('review/edit/<int:id>/', views.edit),
    path('review/update/<int:id>/', views.update_review), 
    path('review/delete/<int:id>', views.delete_review),  

]