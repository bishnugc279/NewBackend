from django.db import models
from clients.models import Client
from accountUsers.models import ClientUser
from datetime import datetime



# Create your models here.
class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True, null=False)
    coupon_name = models.CharField(max_length=64, null=False)
    coupon_code = models.CharField(max_length=64 , null=False)
    start_date = models.DateTimeField(auto_now_add=False, null=False)
    end_date = models.DateTimeField(auto_now_add=False, null=False)
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(default=datetime.now)
    description = models.TextField(null=False)
    coupon_image = models.ImageField(upload_to='image/coupon', blank=True, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    clientuser_id = models.ForeignKey(ClientUser, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.coupon_name





