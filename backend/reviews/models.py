from django.db import models
from accountUsers.models import User
from clients.models import Client
from datetime import datetime

# Create your models here.

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, null=False)
    review_title = models.CharField(max_length=255, null=False)
    review_description = models.TextField(null=False)
    review_rating = models.IntegerField(blank=True, null=True)
    review_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    review_update_date = models.DateTimeField(default=datetime.now)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.review_title


    


