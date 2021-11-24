from django.db import models

class MenuCategory(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    category_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.category_name

class MenuDetail(models.Model):
    menuDetail_id = models.AutoField(primary_key=True, null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.items
    
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True, null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(null=False, max_digits=8, decimal_places=2)
    description = models.TextField(null=False)
    booking_option = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='image\menu', null=False, blank=True)

    def __str__(self):
        return self.menu_name




