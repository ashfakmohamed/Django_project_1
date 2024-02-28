from django.db import models

# Create your models here.
class Database(models.Model):
    mobile = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    monitor = models.CharField(max_length=100)
    price = models.CharField(max_length=100)