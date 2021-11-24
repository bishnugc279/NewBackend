from django.db import models
from datetime import datetime


# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, null=False)
    order_entry_date = models.DateTimeField(default=datetime.now)
    order_demand_date = models.DateTimeField(default=datetime.now)
    order_item = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=100, null=False)
    operator = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.order_item