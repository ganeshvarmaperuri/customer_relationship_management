from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(default='profile_pic.png', upload_to='profile_pics')
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (('Indoor','Indoor'), ('Outdoor', 'Outdoor'))
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS = (('Pending', 'Pending'),
              ('Out for Delivery', 'Out for Delivery'),
              ('Delivered', 'Delivered'))
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.products.name

