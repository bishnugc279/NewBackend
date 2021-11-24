from django.db import models
from accountUsers.models import User
from clients.models import Client
from datetime import datetime



# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, null=False)
    booking_name = models.CharField(max_length=64, default='', null=True)
    reserve_seat = models.CharField(max_length=64, default='', null=True)
    booking_menu = models.CharField(max_length=64, default='',null=True) 
    number_of_people = models.IntegerField(null=False)
    booking_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=64, default='new')
    start_date = models.DateTimeField(auto_now_add=False, default='', null=True)
    end_date = models.DateTimeField(auto_now_add=False, default='', null=True)
    clientuser_email = models.CharField(max_length=64, blank=True, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.booking_name

