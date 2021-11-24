from django.db import models
from accountUsers.models import User
from clients.models import Client
from datetime import datetime



# Create your models here.
class Inbox(models.Model):
    inbox_id = models.AutoField(primary_key=True, null=False)
    inbox_title = models.CharField(max_length=64, null=False)
    inbox_description = models.TextField(null=False)
    inbox_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=64, default='New')
    update_date = models.DateTimeField(default=datetime.now)
    clientuser_address = models.CharField(max_length=255, default='', null=True)
    operater_reply = models.CharField(max_length=255, default='', null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.inbox_title
