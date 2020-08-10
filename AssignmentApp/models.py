from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=120)
    shop_location = models.CharField(max_length=120)

class Category(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL,null=True)
    category_name = models.CharField(max_length=120)
    parent_cat = models.CharField(max_length=120)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    product_name = models.CharField(max_length=120)

class Media(models.Model):
    product_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)