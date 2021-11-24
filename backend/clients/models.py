from django.db import models

# Create your models here.
class BusinessType(models.Model):
    businesstype_id = models.AutoField(primary_key=True, null=False)
    businesstype_name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.businesstype_name
    

class BusinessOwner(models.Model):
    owner_id = models.AutoField(primary_key=True, null=False)
    owner_first_name = models.CharField(max_length=64, null=False)
    owner_last_name = models.CharField(max_length=64, null=False)
    owner_email = models.CharField(max_length=64, null=False)
    owner_phoneno = models.CharField(max_length=64, null=False)
    owner_mobile = models.CharField(max_length=64, null=True)
    owner_address = models.CharField(max_length=64, null=False)
    owner_gender = models.CharField(max_length=64, null=False)
    joined_date = models.DateTimeField(auto_now_add=False, null=False)

    def __str__(self):
        return f"{self.owner_first_name} {self.owner_last_name}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True, null=False)
    client_first_name = models.CharField(max_length=64, null=False)
    client_last_name = models.CharField(max_length=64, null=False)
    pan_number = models.CharField(max_length=64, default='', null=True)
    businesstype_id = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
    email_address = models.CharField(max_length=64, null=False)
    landline_number = models.CharField(max_length=10, default='', null=True)
    mobile_number = models.CharField(max_length=20, default='', null=True)
    country = models.CharField(max_length=64, null=False)
    district = models.CharField(max_length=64, null=False)
    ward = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=255, default='', null=True)
    sub_description = models.CharField(max_length=255, default='', null=True)
    number_of_seats = models.CharField(max_length=100, blank=True, null=True)
    private_rooms =  models.BooleanField(blank=True, null=True)
    open_hour = models.DateTimeField(auto_now_add=False, null=False)
    closing_hour = models.DateTimeField(auto_now_add=False, null=False)
    price_range = models.CharField(max_length=64,  null=False)
    image = models.ImageField(upload_to='image\client', blank=True, null=True)

    def __str__(self):
        return f"{self.client_first_name} {self.client_last_name}"


