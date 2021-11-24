from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime



# Create your models here.

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_clientUser = models.BooleanField(default=False)
    is_systemUser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email_address = models.CharField(max_length=64, null=False, unique=True)


class CustomerUser(models.Model):
    custom_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number= models.IntegerField(null=False)
    country = models.CharField(max_length=64, null=False)
    district = models.CharField(max_length=64, null=False)
    ward = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)
    dob = models.DateField(auto_now_add=False, blank=False)
    gender = models.CharField(max_length=64, null=False)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email_address



class SystemUser(models.Model):
    custom_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    systemuser_gender = models.CharField(max_length=64, null=False)
    systemuser_phone = models.CharField(max_length=64, null=False)
    systemuser_mobile = models.CharField(max_length=64, null=False)
    systemuser_address = models.CharField(max_length=64, null=False)
    role = models.CharField(max_length=64, null=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.systemuser_email



class ClientUser(models.Model):
    custom_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    client_user_gender = models.CharField(max_length=64, null=False)
    client_user_phone = models.CharField(max_length=64, null=False)
    client_user_mobile = models.CharField(max_length=64, null=False)
    client_user_address = models.CharField(max_length=64, null=False)
    role = models.CharField(max_length=54, null=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.client_user_email




