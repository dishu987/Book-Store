from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Favbooks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=100)
    discounted = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_image = models.CharField(max_length=200)
    auther = models.CharField(max_length=100,default="NA")
    date = models.CharField(max_length=100,default="NA")
    rating_count = models.CharField(max_length=100,default="NA")
    rating = models.CharField(max_length=100,default="NA")
    def __str__(self):
        return str(self.id)

class RecentSearch(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

