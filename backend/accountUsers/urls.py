from django.urls import path
from accountUsers import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('customerUser_registration', views.customerUser_registration, name='customerUser_registration'),
    path('systemUser_registration', views.systemUser_registration, name='systemUser_registration'),
    path('clientUser_registration', views.clientUser_registration, name='clientUser_registration'),

]
