from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)



